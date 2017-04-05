import logging

from twisted.web.client import Agent
from twisted.internet import defer, task, reactor
from twisted.internet.error import DNSLookupError


class URLTester(object):
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    @defer.inlineCallbacks
    def __call__(self, url):
        self.log.debug('calling: GET -> %s', url)
        agent = Agent(reactor)
        code = None
        try:
            response_obj = yield agent.request('GET', url)
            code = response_obj.code
            self.log.debug('response code: %s', code)
        except DNSLookupError, err:
            self.log.error('call error: -> %s, reson: %s', url, err)
        defer.returnValue(code)


@defer.inlineCallbacks
def main(_):
    logging.basicConfig(level=logging.DEBUG)
    test_url = URLTester()
    code = yield test_url('http://bb.co')
    print('Response code %s' % code)


if __name__ == '__main__':
    task.react(main)

