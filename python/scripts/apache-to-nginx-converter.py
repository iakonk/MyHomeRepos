#!/bin/env python

from re import search
from glob import glob
import os.path
from os import remove
from commands import getoutput
import hashlib
from sys import exit

vhosts_watch = '/etc/httpd/conf/vhosts.conf'
nginx_config = '/etc/nginx/conf.d/virtual.conf'
php_fpm_pool = '/etc/php-fpm.d/'

nginx_virtual_tpl = '/etc/nginx/conf.d/nginx_virtual_tpl'
php_pool_tpl = 'apache-to-nginx-template-for-converter.tmpl'

md5log = '/tmp/httpd_vhosts_log'
socket = {}

# func to define md5sum for Apache vhost file
# in order to rebuild nginx file if Apache config changed
def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

# Check that old /etc/httpd/conf/vhosts.conf changed
# if changed - write new md5 to the log , covert vhosts to virtual , create new PHP-FPM configs or remove old one, add nginx to service group or remove
# exit otherwise
if not os.path.exists(md5log):
    md5log_write = open(md5log, 'w').close()

lines = [line.rstrip() for line in open(md5log)]
if not lines:
    md5log_write = open(md5log, 'w')
    md5log_write.write('0000')
    md5log_write.close()
    lines = [line.rstrip() for line in open(md5log)]

if md5Checksum(vhosts_watch) != lines[0]:
    print (vhosts_watch + " file changed")
    md5log_write = open(md5log, 'w')
    md5log_write.write(md5Checksum(vhosts_watch))
    md5log_write.close()
    # Convert /etc/httpd/conf/vhosts.conf to /etc/nginx/conf.d/virtual.conf
    vhosts_file = open(vhosts_watch, 'r')
    virtual_nginx = open(nginx_config, 'w')

    print ('\nConverting apache to nginx..')
    for line in vhosts_file:
        if search(r'<VirtualHost', line):
            port = line.split(':')[1].split('\n')[0].split('>')[0]

        if search(r'ServerAlias', line):
            server_alias = line.split('ServerAlias')[1].split('\n')[0]

        if search(r'DocumentRoot', line):
            document_root = line.split()[1]

        if search(r'ErrorLog', line):
            error_log = line.split()[1]

        if search(r'uexecUserGroup', line):
            user = line.split()[1].split('\n')[0]
            group = line.split()[2].split('\n')[0]
            socket[user] = group

        if search(r'</VirtualHost>', line):
            read_tpl = open(nginx_virtual_tpl, 'r')
            replacements = {'$port':port, '$server_alias':server_alias, '$document_root':document_root, '$error_log': error_log, '$socket':'/var/run/' + user +'.sock'}
            for line in read_tpl:
                for src, target in replacements.iteritems():
                    line = line.replace(src, target)
                virtual_nginx.write(line)
            read_tpl.close()
    vhosts_file.close()
    virtual_nginx.close()

    # Create new socket if not exists
    print ('\nChecking if new PHP-FPM socket should be created..')
    for key, val in socket.iteritems():
        php_fpm_dir = php_fpm_pool + key + '.conf'
        if not os.path.exists(php_fpm_dir):
            print('...Creating new socket  ' + php_fpm_dir)
            new_php_fpm = open(php_fpm_dir, 'w')
            read_php_tpl = open(php_pool_tpl, 'r')
            replacements = {'$user_name': key, '$user_group': val, '$user_socket': '/var/run/' + key + '.sock'}
            for line in read_php_tpl:
                for src, target in replacements.iteritems():
                    line = line.replace(src, target)
                new_php_fpm.write(line)
            read_php_tpl.close()
            new_php_fpm.close()
            print getoutput('usermod -a -G ' + val + ' nginx')
    print ('All socket exist!')

    # Remove old socket files
    print ('\nChecking already existing PHP-FPM sockets...')
    for file in glob(php_fpm_pool + "*.conf"):
        existing_socket = file.split(php_fpm_pool)[1].split('.conf')[0]
        if existing_socket not in socket.keys():
            print ('Old socket found and removed ' + file)
            remove(file)
            print ("Removing nginx from group " + existing_socket.split('-www')[0] + '-grp')
            print('gpasswd -d nginx  ' + existing_socket.split('-www')[0] + '-grp')
            print getoutput('gpasswd -d nginx  ' + existing_socket.split('-www')[0] + '-grp')

    # Reload nginx
    print getoutput('/usr/sbin/nginx -s reload')
    print getoutput('/etc/init.d/php-fpm restart')
else:
    exit('Apache vhost file not changed, nothing to update')
