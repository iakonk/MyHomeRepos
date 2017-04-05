import logging
import io

from twisted.web.client import Agent, RedirectAgent
from twisted.internet import defer, task, reactor, protocol
from twisted.internet import _sslverify
from bs4 import BeautifulSoup


# To disable SSL verification
_sslverify.platformTrust = lambda: None


class HTMLdoc(object):
    """ Stores HTML elements"""
    def __init__(self):
        self.text = []
        self.href_attribs = []
        self.json_selectors = []


class HTMLResponseProtocol(protocol.Protocol):
    def __init__(self, on_end_defer):
        self.log = logging.getLogger(self.__class__.__name__)
        self.on_end_defer = on_end_defer
        self.body_buff = io.BytesIO()
        self.html_doc = HTMLdoc()

    def process_body(self):
        self.body_buff.seek(0)
        soup = BeautifulSoup(self.body_buff.getvalue())
        print(soup.prettify())
        for link in soup.find_all('a'):
            print(link.get('href'))
        print soup.get_text().split()
        js_tags = soup.select("script[type=application/json]")
        print js_tags
        self.links.href.append('a')

    def dataReceived(self, bytes):
        self.body_buff.write(bytes)

    def connectionLost(self, reason):
        self.log.debug('Call finished: %s', reason.value)
        self.process_body()
        self.on_end_defer.callback(self.links)


class URLParser(object):
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    @defer.inlineCallbacks
    def __call__(self, url):
        self.log.debug('calling: GET -> %s', url)
        agent = RedirectAgent(Agent(reactor))
        on_end_defer = defer.Deferred()
        response_obj = yield agent.request('GET', url)
        response_obj.deliverBody(HTMLResponseProtocol(on_end_defer))
        links = yield on_end_defer
        defer.returnValue(links.href)


@defer.inlineCallbacks
def main(_):
    logging.basicConfig(level=logging.DEBUG)
    parse_url_act = URLParser()
    code = yield parse_url_act('https://bicswiki.bc')
    print code

if __name__ == '__main__':
    task.react(main)
