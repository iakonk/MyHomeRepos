import logging
import json
import io
import gzip

from twisted.web.client import Agent, RedirectAgent
from twisted.internet import defer, task, reactor, protocol
from twisted.internet import _sslverify
from HTMLParser import HTMLParser


# To disable SSL verification
_sslverify.platformTrust = lambda: None


class HTMLinksContainer(object):
    """ Contains all links found """
    def __init__(self, links):
        self.links = links


class HTMLFeedParser(HTMLParser):
    """ Finds all Links """
    def __init__(self):
        HTMLParser.__init__(self)
        self.log = logging.getLogger(self.__class__.__name__)
        self.tag = None
        self.data_type = None
        self.json_buff = io.BytesIO()
        self.fd = gzip.GzipFile(fileobj=self.json_buff, mode='w')
        self.links = set()

    def handle_starttag(self, tag, attrs):
        self.tag = tag
        for attr in attrs:
            attr_name, attr_val = attr
            if attr_name == 'type' and attr_val == 'application/json':
                self.data_type = 'application/json'
            if attr_name == 'href':
                # we save all links - absolute, relative, bookmarks
                self.links.add(attr_val)
            elif attr_name == 'src':
                # we save all scr links - absolute, relative, bookmarks
                self.links.add(attr_val)
            elif attr_name == 'style':
                # handle links in <style>
                url_start_ind = attr_val.find('url')
                if url_start_ind != -1:
                    ul_end_ind = attr_val.find(')', url_start_ind)
                    url_subst = attr_val[url_start_ind:ul_end_ind]
                    self.links.add(url_subst.lstrip('url('))
            else:
                # handle all rest links
                if attr_val and 'http' in attr_val:
                    self.links.add(attr_val)

    def handle_endtag(self, tag):
        if self.data_type == 'application/json':
            self.parse_js()
            # empty buff
            self.json_buff = io.BytesIO()
        self.tag = None
        self.data_type = None

    def isLink(self, sequence):
        try:
            return sequence.startswith('/') or sequence.startswith('http')
        except Exception:
            return False

    def traverse_js(self, data):
        if isinstance(data, dict):
            for key, val in data.items():
                if isinstance(val, dict):
                    self.traverse_js(val)
                elif isinstance(val, list):
                    self.traverse_js(val)
                else:
                    if self.isLink(val):
                        self.links.add(val)
        elif isinstance(data, list):
            for elem in data:
                self.traverse_js(elem)
        else:
            if self.isLink(data):
                self.links.add(data)

    def parse_js(self):
        self.json_buff.seek(0)
        with gzip.GzipFile(filename=self.json_buff, mode='r') as fd:
            data = json.load(fd)
        self.traverse_js(data)

    def handle_data(self, data):
        # we save only json data, do not care about links as text
        # Feeding incomplete chunks works, but handle_data() might be called more than once
        # handle incomplete chunks
        if self.data_type == 'application/json':
            self.fd.write(data)

    def handle_decl(self, data):
        # handle links in DOCTYPE string
        if 'http' in data:
            self.links.add(data)


class HTMLResponseProtocol(protocol.Protocol):
    """ Handles received bytes from web server """
    def __init__(self, on_end_defer):
        self.log = logging.getLogger(self.__class__.__name__)
        self.on_end_defer = on_end_defer
        self.parser = HTMLFeedParser()

    def dataReceived(self, bytes):
        self.parser.feed(bytes)

    def connectionLost(self, reason):
        self.log.debug('Call finished: %s', reason.value)
        links_obj = HTMLinksContainer(self.parser.links)
        self.parser.close()
        self.on_end_defer.callback(links_obj)


class URLParser(object):
    """ Extracts Links from HTML Doc """
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    @defer.inlineCallbacks
    def __call__(self, url):
        self.log.debug('calling: GET -> %s', url)
        agent = RedirectAgent(Agent(reactor))
        on_end_defer = defer.Deferred()
        response_obj = yield agent.request('GET', url)
        response_obj.deliverBody(HTMLResponseProtocol(on_end_defer))
        links_obj = yield on_end_defer
        defer.returnValue(links_obj)


@defer.inlineCallbacks
def main(_):
    logging.basicConfig(level=logging.DEBUG)
    parse_url_act = URLParser()
    links_obj = yield parse_url_act('http://google.com')
    print 'All links:', links_obj.links


if __name__ == '__main__':
    task.react(main)
