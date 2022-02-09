"""Identify duplicate files."""
import collections
import os

if __name__ == '__main__':
    valid_extensions = {'.tif', '.csv', '.zip'}
    unknown_extensions = set()
    seen_files = set()
    duplicate_files = collections.defaultdict(list)
    with open('files.txt', 'r') as file_list_file:
        for line in file_list_file:
            line = line.rstrip()
            filename = line.split('/')[-1]
            duplicate_files[filename].append(line)
            if filaname not in
            ext = os.path.splitext(filename)[1]
            if ext != '' and ext not in valid_extensions:
                unknown_extensions.add(ext)
                print(line)
    for filename, filelist in duplicate_files.items():
        if len(filelist) > 1:
            print(f'{filename}\n{"\n\t".join(filelist)}')
    #print(f'unknown_extensions: {unknown_extensions}')
