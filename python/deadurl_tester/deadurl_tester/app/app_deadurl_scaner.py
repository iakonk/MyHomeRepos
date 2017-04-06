import os
import signal
import logging
import argparse

from twisted.internet import defer, task

from deadurl_tester import init_logging
from deadurl_tester.actions import test_url_action, parse_url_action


class DeadLinksIdentifier(object):
    def __init__(self, jobs, url):
        self.log = logging.getLogger(self.__class__.__name__)
        self.jobs = jobs
        self.url = url
        self.parse_url_action = parse_url_action.URLParser()
        self.test_url_action = test_url_action.URLTester()
        self.dead_url_list = []

    # this is a some kind of queue obj with X numbers of workers
    @defer.inlineCallbacks
    def find_dead_links(self, url_list, jobs):
        coop = task.Cooperator()
        wait_task_deferreds = []
        for job_number in range(jobs):
            self.log.info('scheduling #%s task', job_number)
            gen = self.find_dead_url_generator(url_list)
            wait_task_deferreds.append(coop.coiterate(gen))
        self.log.info('waiting %s tasks to complete...', len(wait_task_deferreds))
        yield defer.DeferredList(wait_task_deferreds)
        self.log.info('completed %s tasks : dead links finder', len(wait_task_deferreds))

    def find_dead_url_generator(self, url_list):
        while url_list:
            one_url = url_list.pop()
            formatted_url = self.format_link(one_url)
            yield self.test_one_url(formatted_url)

    @defer.inlineCallbacks
    def test_one_url(self, one_url):
        # GET requests will not be started in parallel unless threads.deferToThread is used
        # Or twsited spawnProcess
        # this part can be speed up - it is a single thread now
        response_code = yield self.test_url_action(one_url)
        if not response_code:
            # this is unhandled error
            self.dead_url_list.append(one_url)
        if str(response_code).startswith('4'):
            # this is 4xx Client errors
            self.dead_url_list.append(one_url)
        if str(response_code).startswith('5'):
            # this is 5xx Server error
            self.dead_url_list.append(one_url)

    def format_link(self, href):
        # follow local links
        if href.startswith('/'):
            href = self.url + href
        elif not href.startswith('http'):
            href = self.url + '/' + href
        return href

    @defer.inlineCallbacks
    def run(self):
        self.log.info('extracting all link from: %s', self.url)
        html_doc = yield self.parse_url_action(self.url)
        links = html_doc.links
        self.log.info('found links to test: %s -> %s', len(links), links)
        yield self.find_dead_links(links, self.jobs)
        if self.dead_url_list:
            self.log.info('Found %s dead links: %s', len(self.dead_url_list), self.dead_url_list)
        else:
            self.log.debug('No dead links found')


@defer.inlineCallbacks
def main(reactor, args):
    """ Entry point."""
    logging.basicConfig(level=logging.DEBUG)
    app = DeadLinksIdentifier(args.jobs, args.url)
    yield app.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='append_const', const=1)
    parser.add_argument('-l', '--logdir', default='./', required=False)
    parser.add_argument('-j', '--jobs', default=4, type=int, required=False)
    parser.add_argument('-u', '--url', required=True)
    args = parser.parse_args()
    init_logging(args)
    try:
        task.react(main, [args])
    finally:
        os.killpg(0, signal.SIGKILL)
