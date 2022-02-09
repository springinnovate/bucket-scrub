"""Identify duplicate files."""
import os

if __name__ == '__main__':
    valid_extensions = {'.tif', '.csv', '.zip'}
    unknown_extensions = set()
    with open('files.txt', 'r') as file_list_file:
        for line in file_list_file:
            line = line.rstrip()
            filename = line.split('/')[-1]
            ext = os.path.splitext(filename)[1]
            if ext != '' and ext not in valid_extensions:
                unknown_extensions.add(ext)
                print(line)
    print(f'unknown_extensions: {unknown_extensions}')
