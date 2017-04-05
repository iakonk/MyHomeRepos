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
        self.all_text = []
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
        # print(soup.prettify())
        for link in soup.find_all('a'):
            href = link.get('href')
            self.html_doc.href_attribs.append(href)
        self.html_doc.all_text =  soup.get_text().split()
        self.html_doc.json_selectors = soup.select("script[type=application/json]")

    def dataReceived(self, bytes):
        self.body_buff.write(bytes)

    def connectionLost(self, reason):
        self.log.debug('Call finished: %s', reason.value)
        self.process_body()
        self.on_end_defer.callback(self.html_doc)


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
        html_doc = yield on_end_defer
        defer.returnValue(html_doc)


@defer.inlineCallbacks
def main(_):
    logging.basicConfig(level=logging.DEBUG)
    parse_url_act = URLParser()
    html_doc = yield parse_url_act('https://bicswiki.bc')
    print 'All text:', html_doc.all_text, '\n'
    print 'All href attribs: ', html_doc.href_attribs, '\n'
    print 'All json selectors: ', html_doc.json_selectors, '\n'


if __name__ == '__main__':
    task.react(main)
