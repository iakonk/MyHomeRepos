import logging

from twisted.web.client import Agent, RedirectAgent
from twisted.internet import defer, task, reactor


class URLTester(object):
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    @defer.inlineCallbacks
    def __call__(self, url):
        self.log.debug('calling: GET -> %s', url)
        agent = RedirectAgent(Agent(reactor))
        code = None
        try:
            # State can be either OK
            response_obj = yield agent.request('GET', url)
            code = response_obj.code
            self.log.debug('response code: %s', code)
        except Exception, err:
            # Or state can fail due to any reason: timeouts, dns errors, etc
            # I catch all errors
            self.log.error('call error: -> %s, reson: %s', url, err)
        defer.returnValue(code)


@defer.inlineCallbacks
def main(_):
    logging.basicConfig(level=logging.DEBUG)
    test_url = URLTester()
    code = yield test_url('http://yplanapp.com/og: http://ogp.me/ns# fb: http://ogp.me/ns/fb#')
    print('Response code %s' % code)


if __name__ == '__main__':
    task.react(main)

