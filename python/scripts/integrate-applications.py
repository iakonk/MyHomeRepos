#!/bin/env python
""" 
Script connects new dev PC to local application
"""
import psycopg2
import paramiko
from paramiko.ssh_exception import SSHException, BadHostKeyException, AuthenticationException
from socket import error as socket_error
import optparse
from sys import exit, argv
import datetime
from re import escape

usage = "usage: %prog --sname=XX-{dev name}-pc --alias=XX-{dev name}-pc.XX --ip=x.x.x.x --spass=324358390583477vc"
parser = optparse.OptionParser(usage)
parser.add_option('--sname', action="store", type="str", help='XX-{dev name}-pc')
parser.add_option('--ip', action="store", type="str", help='server IP')
parser.add_option('--alias', action="store", type="str", help='XX-{dev name}-pc.XX')
parser.add_option('--spass', action="store", type="str", help='generate random mysql pass : openssl rand -hex 10')
(options, args) = parser.parse_args()

if not options.sname or not options.ip or not options.alias or not options.spass:
	exit("Some of arguments were not given, run " + argv[0] + ' --help')

   
####
# Local PC side commands
####
planetcontroller = 'X.X.X.X'
ssh_copy_id = "sshpass -p 'XXX' ssh-copy-id -i /var/www/.ssh/id_dsa.pub  root@" + options.ip
spread_rsa_keys = 'cp /root/.ssh/known_hosts /var/www/.ssh/known_hosts; cp /var/www/.ssh/known_hosts /var/www/home/pc/.ssh/known_hosts'
php_config = 'cp /home/pc/www/conf/config_mysql_XXX /home/pc/www/conf/config_mysql_' + (options.sname+'DB').upper() + '.php; chown pc:pc /home/pc/www/conf/config_mysql_' + (options.sname+'DB').upper() + '.php'
edit_php_config = "sed -i 's/$my_host = .*/$my_host = '''" + escape("'") + (options.alias) + escape("'")+ "''';/g'  /home/pc/www/conf/config_mysql_" + (options.sname+'DB').upper() + ".php"
edit_php_config2 = "sed -i 's/$my_pas = .*/$my_pas = '''" + escape("'") + (options.spass) + escape("'")+ "''';/g'  /home/pc/www/conf/config_mysql_" + (options.sname+'DB').upper() + ".php"

####
# Local PC-DB side commands
####
conn_string = "host='XX' dbname='XX' user='root' password='XX'"
select_id="select max(id) from servers"
insert_into_pcdb = """\
INSERT INTO servers(id, operating_system_id, location_id, priority, name, date_established, 
	                  active, ip, subservice_id, 
                    alias_name, nagios_name, def_path, backup_name, server_type, 
                    run_url, provider_id, params, reseller_id, local_ip)  
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

apacheconf_conn = "host='XX' dbname='XX' user='root' password='XX'"
insert_into_pcapacheconf = "INSERT INTO SERVERS(id,name,db,dbserver) VALUES (%s,%s,%s,%s)"
insert_into_switches = "INSERT INTO switch(server_id, updated) VALUES (%s, %s);"

####
# Remote new dev host side
####
copy_config_pl = "cp /home/pc/pc-configs-install/config.pl /home/pc/pc-scripts/"
replace_sname_in_config = "sed -i 's/$sname = .*/$sname = '''" + escape("'") + (options.sname).upper() + escape("'")+ "''';/g' /home/pc/pc-scripts/config.pl"
replace_db_name_in_config = "sed -i 's/$db_sname = .*/$db_sname = '''" + escape("'") + (options.sname+'DB').upper() + escape("'")+"''';/g' /home/pc/pc-scripts/config.pl"
grant_mysql = 'mysql -e "grant all on *.* to root@' + planetcontroller +  ' identified by '+ escape('"') + options.spass + escape('"') + ';"'

"""Local planetcontroller database side:
   Insert into apache.conf.servers: KIEV-DEV-{dev name}-PC
"""
print '\nConfiguring PC-DB:'
try:
       con = psycopg2.connect(apacheconf_conn)
       cur = con.cursor()
       cur.execute(select_id)
       (id,) = cur.fetchone()
       increment_pc = id + 1
       increment_switches = increment_pc + 1
       row = [(increment_pc),((options.sname).upper()),(''),('')]
       switches_row = [(increment_switches),(1)]
       try:
               cur.executemany(insert_into_pcapacheconf, (row,))
	             cur.executemany(insert_into_switches, (switches_row,))
               con.commit()
	             print ("\tSuccess: " + insert_into_pcapacheconf + row)
       except:
               con.rollback()
       con.close()
except psycopg2.DatabaseError, e:
       print 'Error %s' % e

"""Local planetcontroller database side:
   Insert into XX.servers : XX-{dev name}-PC, 
   Insert into XX.servers : XX-{dev name}-PCDB
"""
try:
	con = psycopg2.connect(conn_string)
        cur = con.cursor()
	cur.execute(select_id)
	(id,) = cur.fetchone()
	increment_pc = id + 1
	increment_pcdb = increment_pc + 1
	row_pc = [(increment_pc),(1),(8),(2),((options.sname).upper()),(datetime.date.today()),('TRUE'),(options.ip),(1),(options.alias),(''),('/var/www/home/'),(''),(''),(''),(2),(''),(9),(options.ip)]
	row_pcdb = [(increment_pcdb),(1),(8),(2),((options.sname+'DB').upper()),(datetime.date.today()),('TRUE'),(options.ip),(5),(options.alias),(''),('/var/www/home/'),(''),(''),(''),(2),(''),(9),(options.ip)]
	try:
		cur.executemany(insert_into_pcdb, (row_pc,))
		cur.executemany(insert_into_pcdb, (row_pcdb,))
		con.commit()
		print ("\tSuccess: " + insert_into_pcdb + row_pc + row_pcdb)
	except:
		con.rollback()
	con.close()
except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    exit(1)
print '-----------------------------------'

"""New dev host side: 
   Configure /home/pc/pc-scripts/config.pl : copy, insert sname
"""
print '\nConfiguring new dev host ' + options.ip +  ': '
try:
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(options.ip)
	stdin, stdout, stderr = ssh.exec_command(copy_config_pl)
	if stdout.channel.recv_exit_status() > 0:
		print ("\tSomething went wrong: " + copy_config_pl)
	else:
		print ("\tSuccess: " + copy_config_pl)
	stdin, stdout, stderr = ssh.exec_command(replace_sname_in_config)
	if stdout.channel.recv_exit_status() > 0:
                print ("\tSomething went wrong: " + replace_sname_in_config)
	else:
		print ("\tSuccess: "  + replace_sname_in_config)
	stdin, stdout, stderr = ssh.exec_command(replace_db_name_in_config)
        if stdout.channel.recv_exit_status() > 0:
                print ("\tSomething went wrong: " + replace_db_name_in_config)
	else:
		print ("\tSuccess: "+ replace_db_name_in_config)
	stdin, stdout, stderr = ssh.exec_command('cat /root/.ssh/id_rsa.pub')
	pub_ssh_content =  stdout.readlines()

	stdin, stdout, stderr = ssh.exec_command(grant_mysql)
        if stdout.channel.recv_exit_status() > 0:
                print ("\tSomething went wrong: " + grant_mysql)
        else:
                print ("\tSuccess: "  + grant_mysql)

	ssh.close()
except (BadHostKeyException, AuthenticationException,SSHException, socket_error) as e:
       	print "ssh fail ", options.ip
print '-----------------------------------'


"""Local PC side: 
   Configure ssh keys
"""
print '\nConfiguring PC (php config, ssh keys):'
try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(planetcontroller)
	print ("\tAdding dev RSA to PC /root/.ssh/known_hosts")
	stdin, stdout, stderr = ssh.exec_command('ssh-keyscan -t rsa ' + options.ip)
	pub_ssh_content =  stdout.readlines()
	dev_keys = ''
	for line in pub_ssh_content:
	        dev_keys = ' '.join(line.split())
	stdin, stdout, stderr = ssh.exec_command('echo ' + dev_keys + ' >>/root/.ssh/known_hosts')	
	if stdout.channel.recv_exit_status() > 0:
                print ("\tFail: " + 'echo ' + dev_keys + ' >>/root/.ssh/known_hosts' )
        else:
                print ("\tSuccess: " + 'echo ' + dev_keys + ' >>/root/.ssh/known_hosts')

	print ("\tTrying  " + ssh_copy_id)
        stdin, stdout, stderr = ssh.exec_command(ssh_copy_id)
	if stdout.channel.recv_exit_status() > 0:
		print ("\tFail: " + ssh_copy_id)
	else:
		print ("\tSuccess: " + ssh_copy_id)

	stdin, stdout, stderr = ssh.exec_command(spread_rsa_keys)
	if stdout.channel.recv_exit_status() > 0:
                print ("\tSomething went wrong when : " + spread_rsa_keys)
	else:
		print ("\tSuccess: " + spread_rsa_keys)

        stdin,stdout,stderr = ssh.exec_command(php_config)
	if stdout.channel.recv_exit_status() > 0:
                print ("\tSomething went wrong when : " + php_config)
	else:
		print ("\tSuccess: " + php_config)
	
	stdin,stdout,stderr = ssh.exec_command(edit_php_config)
        if stdout.channel.recv_exit_status() > 0:
                print ("\tSomething went wrong when : " + edit_php_config)
        else:
                print ("\tSuccess: " + edit_php_config)

	stdin,stdout,stderr = ssh.exec_command(edit_php_config2)
        if stdout.channel.recv_exit_status() > 0:
                print ("\tSomething went wrong when : " + edit_php_config2)
        else:
                print ("\tSuccess: " + edit_php_config2)

        ssh.close()
except (BadHostKeyException, AuthenticationException,SSHException, socket_error) as e:
        print "ssh fail ", planetcontroller
print '-----------------------------------'
