"""Identify duplicate files."""
import collections
import os
import re

if __name__ == '__main__':
    valid_extensions = {'.tif', '.csv', '.zip', '.gpkg'}
    unknown_extensions = set()
    seen_files = set()
    filesize_dict = collections.defaultdict(list)
    total_size = 0
    with open('file_size.txt', 'r') as file_list_file:
        for line in file_list_file:
            line = line.rstrip()
            if line.endswith('/'):
                continue
            x = re.match('([^ ]+) +([^ ].*)', line)
            size, filepath = x.groups()
            filesize_dict[int(size)].append(filepath)
            total_size += int(size)

    for filesize in sorted(filesize_dict):
        print(filesize/2**30, filesize_dict[filesize])
    print(total_size)
    #print(f'unknown_extensions: {unknown_extensions}')
