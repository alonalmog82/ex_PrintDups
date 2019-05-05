#!/usr/bin/env python
#
# Based on examples taken from:
# http://www.davespace.co.uk/python/remove-duplicates.html
# https://stackoverflow.com/questions/16874598/how-do-i-calculate-the-md5-checksum-of-a-file-in-python/16876405

import hashlib
import os
import stat
import sys
from collections import defaultdict


def usage():
    print('Usage: PrintDups.py DIRECTORY')
    sys.exit(1)

def main(argv):
    if len(argv) < 1:
        usage()

    dir = os.path.abspath(argv[0])

    size_hm = defaultdict(list)
    md5_hm = defaultdict(list)
    
    for root, dirs, files in os.walk(dir):
        for name in files:
            path = os.path.join(root, name)
            #print(name)
            size = os.path.getsize(path)
            #print(size)
            file_tupple = (path, name)
            #print(file_tupple[1])
            size_hm[size].append(file_tupple)

    for item in size_hm:
        #print(size_hm[item])
        if (len(size_hm[item]) > 1 ):
            for i in range(len(size_hm[item])):
                file_tupple = (size_hm[item][i])
                file_path = (file_tupple[0])
                file_name = (file_tupple[1])
                md5hash = hashlib.md5(open(file_path,'rb').read()).hexdigest()
                md5_hm[md5hash].append(file_name)
    
    for item in md5_hm:
        for i in range(len(md5_hm[item])):
            print(md5_hm[item][i]),
            if ((i+1) < (len(md5_hm[item]))) :
                print(','),
        print('\n')

if __name__ == '__main__':
    main(sys.argv[1:])
