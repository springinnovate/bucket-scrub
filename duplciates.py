"""Identify duplicate files."""
import collections
import os
import re

def main():
    """Entry point."""
    valid_extensions = {'.tif', '.csv', '.zip', '.gpkg', '.gz'}
    unknown_extensions = set()
    seen_files = set()
    filesize_dict = collections.defaultdict(list)
    total_size = 0
    unknown_file_list = []

    skip_substrings = [
        'ipbes-natcap-ecoshard-data-for-publication',
        'gee_export',
        'living_database',
        'global_carbon_regression_2',
        ]
    keep_files = set()
    with open('file_size.txt', 'r') as file_list_file:
        for line in file_list_file:
            line = line.rstrip()
            if os.path.basename(line) in keep_files:
                continue
            if os.path.splitext(line)[1] == '':
                continue
            if any([substring in line for substring in skip_substrings]):
                print(line)
                keep_files.add(os.path.basename(line))
                continue
            x = re.match('([^ ]+) +([^ ].*)', line)
            size, filepath = x.groups()
            ext = os.path.splitext(filepath)[1]
            if ext != '' and ext not in valid_extensions:
                unknown_extensions.add(ext)
                unknown_file_list.append(filepath)
            filesize_dict[int(size)].append(filepath)
            total_size += int(size)
            seen_files.add(os.path.basename(filepath))

    #for filesize in sorted(filesize_dict):
    #    print(filesize/2**30, filesize_dict[filesize])
    #print(total_size)
    #print(unknown_file_list)
    #print(f'unknown_extensions: {unknown_extensions}')
    with open('unique_files.txt', 'w') as unique_files_file:
        for file_path in seen_files:
            if file_path in keep_files:
                continue
            unique_files_file.write(f'{file_path}\n')


if __name__ == '__main__':
    main()
