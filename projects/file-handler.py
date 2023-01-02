import argparse
import os


def get_file_list(filename):
    for root, dirs, files in os.walk(filename):
        for name in files:
            print(os.path.join(root, name))


def file_handler():
    """python3 file-handler.py <filename>"""
    parser = argparse.ArgumentParser(description='File Handler')
    parser.add_argument('filename', nargs='?')
    args = parser.parse_args()
    if args.filename:
        get_file_list(args.filename)
    else:
        print('Directory is not specified')


if __name__ == '__main__':
    file_handler()
