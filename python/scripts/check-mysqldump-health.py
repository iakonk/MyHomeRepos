#!/bin/env python

import psycopg2
import sys,os
from subprocess import Popen, PIPE
from datetime import datetime
import smtplib

con = None
today = datetime.now().strftime("%Y-%m-%d")

log_dump_fail = '/tmp/mysqldump_FAIL'
log_fail = open(log_dump_fail,'w').close()
log_fail = open(log_dump_fail, 'a')

sender = 'PUT_SENDER_NAME_HERE'
receiver = ['receiver_name']
smtp_daemon_host = 'localhost'

def db_backup_file_does_not_exist(db_backup_file):
    if not os.path.exists(db_backup_file): return True
    else: return False

def dump_health(last_dump_row, file_name,db):
       last_row = last_dump_row.rsplit(" ")
       tms = ''.join(last_row[4:5])
       status = last_row[1:3]
       
       if (status) and (tms != today):
	  log_fail.write("\nDB is old for "+ str(db) + str(file_name) + ", \nDump finished at " + str(''.join(tms)))
	  log_fail.write("\n-------------------------------------------")
       elif not (status) and (tms == None):
	  log_fail.write("\nDump is not complete for "+str(db) +  str(file_name) + " , end of file is not correct") 
	  log_fail.write("\n-------------------------------------------")

suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
    if nbytes == 0: return '0 B'
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

def dump_size(dump_file, file_name,db):
       size = os.path.getsize(dump_file)
       if (size < 1024):
	  human_readable = humansize(size)
          log_fail.write("\nDump is empty for " +str(db) + "\n" +"\t" + str (file_name)+", file size is " + str(human_readable))
	  log_fail.write("\n-------------------------------------------")

def report_to_noc(isubject,text):
	TEXT = text
        SUBJECT = subject
        message = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
        server = smtplib.SMTP(smtp_daemon_host)
        server.sendmail(sender, receiver, message)
        server.quit()

try:	
    con = psycopg2.connect(database='**', user='***', password='***', host='****') 
    cur = con.cursor()
    cur.execute("""\
select ad.servicename, (select name from servers where id = ps.server_id) as servername 
from packages as p, account_data as ad, package_servers as ps 
where p.id=ad.package_id and 
p.date_deleted IS NULL and 
p.id=ps.package_id and 
p.aktuel IS NULL and 
p.pre_def_package_id = 4 and  
p.mother_package_id !=0 and 
ps.subservice_id=5 and  
p.mother_package_id NOT IN (select id from packages where date_deleted IS NOT NULL) 
ORDER BY servername; 
""")
        
    while (1):
    	row = cur.fetchone ()
        if row == None:
       		break
        
	db = row[0]
        server_name = str(row[1])
	if (''.join(server_name) == 'BMCLUSTERDB') or (''.join(server_name) == 'GAGDKDB'):
		continue
	else:
		db_backup_file = '/storage/backup/db/mysql/' + str(db) + '/current/' + str(db) + '.mysql.gz'
		db_backup_file2 = '/storage/backup/' + str(''.join(server_name.split("DB"))) + '/mysql/' + str(db) + '/current/'+ str(db) + '.mysql.gz'
        
	db_file_does_not_exist = False
	db_file2_does_not_exist = False
    	
	if db_backup_file_does_not_exist(db_backup_file):
		db_file_does_not_exist = True	
	if db_backup_file_does_not_exist(db_backup_file2):
		db_file2_does_not_exist = True
        
        if db_file_does_not_exist and db_file2_does_not_exist:
                log_fail.write("\nMySQL dump does not exist for " + str(db) +  "\n" + "\t" + str(db_backup_file2) + "\n" + "\t" +  str(db_backup_file))
		log_fail.write("\n-------------------------------------------")
		continue
	elif (db_file_does_not_exist) and not (db_file2_does_not_exist):
		p_zcat = Popen(["zcat", db_backup_file2], stdout=PIPE)
                p_tail = Popen(["tail", "-2"], stdin=p_zcat.stdout, stdout=PIPE)
                dump_status =  str(p_tail.communicate()[0])
                dump_health(dump_status,db_backup_file2,db)
                dump_size(db_backup_file2, db_backup_file2,db)
        elif (db_file2_does_not_exist) and not (db_file_does_not_exist):
		p_zcat = Popen(["zcat", db_backup_file], stdout=PIPE)
                p_tail = Popen(["tail", "-2"], stdin=p_zcat.stdout, stdout=PIPE)
                dump_status =  str(p_tail.communicate()[0])
                dump_health(dump_status,db_backup_file,db) 
		dump_size(db_backup_file,db_backup_file,db)       

    con.close()

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)

log_fail.close()

if os.path.getsize(log_dump_fail) > 0:
        subject = "Not all MySQL dumps completed successfully. Log file backup:" + str(log_dump_fail)
        fh = open(log_dump_fail, 'r')
        text = fh.read()
        fh.close()
        report_to_noc(subject,text)
else:
        subject = "MySQL dump completed successfullyi for all DBs, listed in PC"
        text = "Hello! \nI am notifying you that I checked mysqldump files this morning.\nThere are nothing to worry about. :)"
        report_to_noc(subject,text)
