import argparse
import socket


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

    def send_data(self, data):
        with socket.socket() as client_socket:
            address = (self.host, self.port)
            client_socket.connect(address)
            data = data.encode()
            client_socket.send(data)
            response = client_socket.recv(1024)
            response = response.decode()
            return response


def password_hacker():
    parser = argparse.ArgumentParser(description='Password hacker')
    parser.add_argument('ip', nargs='?')
    parser.add_argument('port', nargs='?')
    parser.add_argument('data', nargs='?')
    args = parser.parse_args()
    if args.ip and args.port and args.data:
        sender = MySocket(args.ip, int(args.port))
        print(sender.send_data(args.data))
    else:
        print(f'Args not supplied')


if __name__ == '__main__':
    password_hacker()
