"""
Script splits files on ".",
Creates dir structure for every part (except last two elements)
Creates symlinks in /graphite_rrd for found files in /apps_rrd_path/*.rrd

Example for proviso.memory-HD.hd.2004795329.rrd:
        mkdir -p proviso/memory/HD/hd
        ln -s  srce_path/proviso.memory.hd.2004795329.rrd  dest_path/proviso/memory/HD/hd/2004795329.rrd

Script arguments:
    SOURCE_PATH - path to application *.rrd files
    DEST_PATH - path, where script will create new symlinks and Graphite will read from
"""
from os import path, makedirs, symlink
from glob import glob
from sys import argv

SOURCE_PATH = glob(argv[1] + '/*.rrd')
DEST_PATH = argv[2]

new_link = 0
exist_link = 0
for file in SOURCE_PATH:
        changed_file = path.basename(file).replace('-', '.').split('.')
        changed_file_parts = '/'.join(changed_file[:-2])
        new_fname = '.'.join(changed_file[-2:])
        new_fpath = path.join(DEST_PATH, changed_file_parts)
        print '\nProcessing file %s' % file
        print 'New path(%s), New file name(%s)' % (new_fpath, new_fname)
        try:
                makedirs(new_fpath)
                symlink(file, path.join(new_fpath, new_fname))
                new_link += 1
        except OSError:
                print 'ERROR: dir already exist (%s)' % new_fpath
                try:
                        symlink(file, path.join(new_fpath, new_fname))
                        new_link += 1
                except:
                        print 'ERROR: symlink already exists (%s)' % path.join(new_fpath, new_fname)
                        exist_link += 1
                        pass
print '*'*100
print 'Found %s sources' % len(SOURCE_PATH)
print 'Symlinks created (%s)' % new_link
print 'Symlinks already exist (%s)' % exist_link
