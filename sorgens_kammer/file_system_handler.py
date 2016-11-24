"""
Prototype of a file system handler.
Creates files and dirs, retrieves information on them,
retrieves dir listings.
TODO: add various metadata.
TODO: handle multiple possible error cases.
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

import time
import os
import logging


class FileSystemHandler(object):

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.filesystem = client.filesystem
        self.files = self.filesystem.files
        self.dirs = self.filesystem.dirs
        self.logger = logging.getLogger('FileSystemHandler')
        log_handler = logging.FileHandler('FileSystem.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        log_handler.setFormatter(formatter)
        self.logger.addHandler(log_handler)

    def create_file(self, path):
        # TODO: handle a case of file and dir having the same name
        if not os.path.exists(path):
            open(path, 'w').close()
            filename = os.path.basename(path)
            abspath = os.path.abspath(path)
            self.files.insert({'abspath': abspath,
                               'timestamp': time.time(),
                               'filename': filename})
            self.logger.info('File %r created', abspath)

            # update listing info for parent dir
            parent_dir = os.path.dirname(abspath)
            # TODO: catch errors here?
            dir_doc = self.dirs.find({'abspath': parent_dir})[0]
            dir_doc['listing'].append(filename)
            self.dirs.save(dir_doc)
            return True
        else:
            self.logger.error('File %r exists', path)
            return False

    def create_dir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
            dirname = os.path.basename(path)
            abspath = os.path.abspath(path)
            self.dirs.insert({'abspath': abspath,
                              'timestamp': time.time(),
                              'dirname': dirname,
                              'listing': []})
            self.logger.info('Dir %r created', abspath)
            return True
        else:
            self.logger.error('Dir %r exists', path)
            return False

    def get_info(self, item_id, collection):
        # TODO: listing is now part of info, redesign?
        return self.filesystem[collection].find_one({'_id': ObjectId(item_id)})

    def get_listing(self, directory_id):
        return self.dirs.find_one({'_id': ObjectId(directory_id)})['listing']
