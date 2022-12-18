import argparse


def decode_caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    decoded = ''
    for c in s:
        decoded += alpha[(alpha.index(c) + n) % len(alpha)]
    # print('Decoded text: "' + text + '"')
    return decoded


def get_encoded_text(filename):
    opened_file = open(filename)
    encoded_text = opened_file.read()  # read the file into a string
    opened_file.close()  # always close the files you've opened
    return encoded_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file")
    args = parser.parse_args()
    text = get_encoded_text(args.file)
    offset_string = args.file.split('.')[0]
    offset = -int(offset_string)
    decoded_text = decode_caesar_cipher(text, offset)
    print(decoded_text)

