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


class HTMLContent(object):
    def __init__(self, json_data, links):
        self.links = links
        self.json_data = json_data


class HTMLFeedParser(HTMLParser):
    """ """
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
                if attr_val and 'http' in attr_val:
                    self.links.add(attr_val)

    def handle_endtag(self, tag):
        self.tag = None
        self.data_type = None

    def traverse(self, obj):
        if isinstance(obj, dict):
            for key, value in obj.iteritems():
                self.log.debug('dict_key', key)
                self.traverse(value)
        elif isinstance(obj, list):
            for value in obj:
                self.traverse(value)
        else:
            self.log.debug('value', obj)

    def parse_js_content(self, data):
        # !!! it should be recursion here
        # it is a very rough implementation
        js_data = json.loads(data)
        for key, val in js_data.items():
            if isinstance(val, dict):
                for key_, val_ in val.items():
                    if isinstance(val_, list):
                        for item in val_:
                            if isinstance(item, dict):
                                for k, v in item.items():
                                    self.log.debug(type(v))
                            else:
                                self.log.debug('%s', type(item))
                    elif isinstance(val_, dict):
                        for k, v in val_.items():
                            self.log.debug(type(v))
                    else:
                        self.log.debug('%s', type(val_))
            elif isinstance(val, list):
                for item in val:
                    self.log.debug('%s', type(item))
            else:
                self.log.debug('%s', type(val))

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
    def __init__(self, on_end_defer):
        self.log = logging.getLogger(self.__class__.__name__)
        self.on_end_defer = on_end_defer
        self.parser = HTMLFeedParser()

    def dataReceived(self, bytes):
        self.parser.feed(bytes)

    def connectionLost(self, reason):
        self.log.debug('Call finished: %s', reason.value)
        html_doc = HTMLContent(self.parser.json_buff, self.parser.links)
        self.parser.close()
        self.on_end_defer.callback(html_doc)


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
    html_doc = yield parse_url_act('http://yplanapp.com')
    print 'All links:', html_doc.links, '\n'
    print 'Json data: ', html_doc.json_data, '\n'


if __name__ == '__main__':
    task.react(main)
