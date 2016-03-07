"""
Listen for file created | deleted events in source_path directory
On create: create corresponding file path and symlink
Example for proviso.memory-HD.hd.2004795329.rrd:
    On create:
        mkdir -p proviso/memory/HD/hd
        ln -s  source_path/proviso.memory-HD.hd.2004795329.rrd  dest_path/proviso/memory/HD/hd/2004795329.rrd
    On delete:
        rm -rf dest_path/proviso/memory/HD/hd/2004795329.rrd
        rm -rf dest_path/proviso if empty

Reference: http://pythonhosted.org/watchdog/
Script arguments:
    SOURCE_PATH - path to application *.rrd files
    DEST_PATH - path, where script will create new symlinks and Graphite will read from
"""
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from os import path, makedirs, symlink, remove, listdir, rmdir
from sys import argv

SOURCE_PATH = argv[1]
DEST_PATH = argv[2]
PATTERN = "*.rrd"


class ChangesHandler(PatternMatchingEventHandler):
    def process(self, event):
        changed_file = path.basename(event.src_path).replace('-', '.').split('.')
        changed_file_parts = '/'.join(changed_file[:-2])
        new_fname = '.'.join(changed_file[-2:])
        new_fpath = path.join(DEST_PATH, changed_file_parts)

        if 'created' in event.event_type:
            if not path.exists(new_fpath):
                makedirs(new_fpath)
            symlink(event.src_path, path.join(new_fpath, new_fname))

        if 'deleted' in event.event_type:
            try:
                remove(path.join(new_fpath, new_fname))
                self.remove_empty_dirs(changed_file[:len(changed_file[:-2])])
            except OSError:
                pass

    def on_created(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)

    @staticmethod
    def remove_empty_dirs(dirs):
        if not listdir(path.join(DEST_PATH, *dirs)):
            rmdir(path.join(DEST_PATH, *dirs))
            for part in range(1, len(dirs)):
                rmdir(path.join(DEST_PATH, *dirs[:-part]))


if __name__ == '__main__':
    observer = Observer()
    observer.schedule(ChangesHandler(), path=SOURCE_PATH)
    observer.start()
    observer.join()
