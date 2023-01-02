import argparse
import os
import hashlib


class FileHandler:
    def __init__(self, filename='.'):
        self.filename = filename
        self.files = self.get_files()
        self.filtered_files = {}

    def __str__(self):
        return f'File:({self.filename})'

    def get_files(self):
        files_information = {}
        for root, dirs, files in os.walk(self.filename):
            for name in files:
                file = os.path.join(root, name)
                file_size = os.path.getsize(file)
                files_information[file] = file_size
        return files_information

    def print_file_list(self):
        for file in self.files:
            print(file)

    def print_file_list_by_extension(self, extension, order):
        rev_multidict = {}
        for key, value in self.files.items():
            if key.endswith(extension):
                rev_multidict.setdefault(value, set()).add(key)

        sort_order = True if order == 'descending' else False
        filtered_files = {}
        for key, value in sorted(rev_multidict.items(), reverse=sort_order):
            if len(value) > 1:
                print(f'{key} bytes')   # print the size of the file
                for each_file in value:
                    print(f'{each_file}')
                filtered_files[key] = value
                print()
        self.filtered_files = filtered_files

    def check_duplicates(self):
        index = 1
        for key, value in self.filtered_files.items():
            hash_dict = {}
            for each_file in value:
                file_hash = hashlib.md5(open(each_file, 'rb').read()).hexdigest()
                hash_dict.setdefault(file_hash, set()).add(each_file)
            print_byte = True
            for h_key, h_value in hash_dict.items():
                if len(h_value) > 1:
                    if print_byte:
                        print(f'{key} bytes')
                        print_byte = False
                    print(f'Hash: {h_key}')
                    for each_dupe_file in h_value:
                        print(f'{index}. {each_dupe_file}')
                        index += 1
            print()


def get_sort_options():
    print('Enter file format:')
    file_format = input()
    print('Size sorting options:')
    print('1. Descending')
    print('2. Ascending')
    while True:
        print('Enter a sorting option:')
        sorting_option = input()
        if sorting_option == '1' or sorting_option == '2':
            return {'format': file_format, 'option': 'descending' if sorting_option == '1' else 'ascending'}
        else:
            print('Wrong option')


def file_handler():
    """python3 file-handler.py <filename>"""
    parser = argparse.ArgumentParser(description='File Handler')
    parser.add_argument('filename', nargs='?')
    args = parser.parse_args()
    if args.filename:
        handler = FileHandler(args.filename)
        sorting_dictionary = get_sort_options()
        handler.print_file_list_by_extension(sorting_dictionary['format'],
                                             sorting_dictionary['option'])
        while True:
            print('Check for duplicates?')
            dupe_check = input()
            if dupe_check == 'yes':
                handler.check_duplicates()
                break
            elif dupe_check == 'no':
                break
            else:
                print('Wrong option')

    else:
        print('Directory is not specified')


if __name__ == '__main__':
    file_handler()
