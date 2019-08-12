#run as:
#bigfiles.py <number of big files> <directory>
#or:
#bigfiles.py 5 /tmp 

import heapq
import os, os.path
import sys
import operator

def file_sizes(directory):
    for path, _, filenames in os.walk(directory):
        for name in filenames:
            full_path = os.path.join(path, name)
            yield full_path, os.path.getsize(full_path)

#sys.argv[1:] means get everything after argument the script name
num_files, directory = sys.argv[1:]
num_files = int(num_files)

big_files = heapq.nlargest(
        num_files, file_sizes(directory), key=operator.itemgetter(1))

print(*("{}\t{:>}".format(*b) for b in big_files))