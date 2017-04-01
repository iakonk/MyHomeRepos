import json
import argparse
import yaml
import logging
import os
import signal
import time

import txtemplate

from twisted.internet import reactor
from twisted.web.server import Site, NOT_DONE_YET
from twisted.web.resource import Resource

from restapi_project.pools import create_pool
from restapi_project import init_logging


POOL_SIZE = 2
TEMPLATE_DIR = os.path.join('restapi_project', "templates")


class Response(object):
    def __init__(self, lines):
        self.lines = lines


class AppUserRegForm(Resource):
    isLeaf = True

    def __init__(self, cfg):
        self.log = logging.getLogger(self.__class__.__name__)
        self.table = cfg['database']['table']
        self.db_filename = cfg['database']['filename']
        self.db_pool = create_pool(POOL_SIZE, self.db_filename)
        self.loader = txtemplate.Jinja2TemplateLoader(TEMPLATE_DIR)
        self.log.debug('%s', TEMPLATE_DIR)

    def _run_query(self, txn, sql):
        ct = time.time()
        txn.execute(sql)
        columns = [i[0] for i in txn.description]
        records_obj = Response([dict(zip(columns, row)) for row in txn.fetchall()])
        self.log.debug('call: finished in %.4fs, %s records found in %s', time.time()-ct, len(records_obj.lines), self.table)
        return records_obj

    def run_query(self, sql):
        self.log.info('Calling table : %s', self.table)
        return self.db_pool.runInteraction(self._run_query, sql)

    def get_all_registrations(self, data_obj, request):
        template_name = "all_registrations.html"
        template = self.loader.load(template_name)

        records = json.dumps(data_obj.lines)
        d = template.render(records_list=records)
        d.addCallback(self.write_response, request)

    def register(self, request):
        template_name = "register.html"
        template = self.loader.load(template_name)
        context = {"greeting": "Hello"}

        d = template.render(**context)
        d.addCallback(self.write_response, request)

    def render_home_page(self, request):
        template_name = "home.html"
        template = self.loader.load(template_name)
        context = {"home": "home page"}

        d = template.render(**context)
        d.addCallback(self.write_response, request)

    def write_response(self, content, request):
        request.write(content)
        request.setResponseCode(200)
        request.finish()

    def render_GET(self, request):
        if request.postpath[0] == 'all_registered':
            sql = 'SELECT * FROM {}'.format(self.table)
            res = self.run_query(sql)
            res.addCallback(self.get_all_registrations, request)
        elif request.postpath[0] == 'register':
            self.register(request)
        else:
            self.render_home_page(request)
        return NOT_DONE_YET


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='append_const', const=1)
    parser.add_argument('-l', '--logdir', default='./', required=False)
    parser.add_argument('-c', '--config', nargs='?', type=argparse.FileType('r'), default='etc/config.yml')
    args = parser.parse_args()
    config = yaml.safe_load(args.config)
    init_logging(args)
    try:
        resource = AppUserRegForm(config)
        factory = Site(resource)
        reactor.listenTCP(8880, factory)
        reactor.run()
    finally:
        os.kill(0, signal.SIGKILL)
