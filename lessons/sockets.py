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
        self.socket = socket.socket()
        self.password = 'mIcHaEl'

    def listen(self):
        print('listening')
        address = (self.host, self.port)
        self.socket.bind(address)
        self.socket.listen(2)
        conn, address = self.socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("from connected user: " + str(data))
            data = input('From listen -> ')
            conn.send(data.encode())  # send data to the client
        conn.close()

    def listen_for_password(self):
        print(f'listening for password {self.password}')
        address = (self.host, self.port)
        self.socket.bind(address)
        self.socket.listen(2)
        conn, address = self.socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        attempts = 0
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("from connected user: " + str(data))
            # data = input('From listen -> ')
            if attempts > 1000000:
                server_message = 'Too many attempts'
                conn.send(server_message.encode())
                break
            if data == self.password:
                server_message = 'Connection success!'
                conn.send(server_message.encode())
            elif data != self.password:
                server_message = f'{data} - Wrong password!'
                conn.send(server_message.encode())
            attempts += 1
        conn.close()

    def send(self):
        address = (self.host, self.port)
        self.socket.connect(address)
        print('sending')
        data = 'Wake up, Neo'
        data = data.encode()
        self.socket.send(data)
        data = self.socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        self.socket.close()

    def context_send(self):
        with socket.socket() as client_socket:
            address = (self.host, self.port)
            client_socket.connect(address)
            data = 'Wake up, Neo'
            data = data.encode()
            client_socket.send(data)
            response = client_socket.recv(1024)
            response = response.decode()
            print(response)


def sockets():
    hostname = '127.0.0.1'
    port = 9090
    client_socket = socket.socket()

    address = (hostname, port)
    client_socket.connect(address)

    data = 'Wake up, Neo'
    # converting to bytes
    data = data.encode()
    # sending through socket
    client_socket.send(data)

    response = client_socket.recv(1024)
    # decoding from bytes to string
    response = response.decode()
    print(response)

    client_socket.close()


def use_sockets():
    mode = input('Mode (R)eceive / (s)end: ').lower()

    if mode == 'send' or mode == 's':
        sender = MySocket(socket.gethostname(), 3022)
        sender.send()
    elif mode == 'receive' or mode == 'r' or mode == '':
        receiver = MySocket(socket.gethostname(), 3022)
        # receiver.listen()
        receiver.listen_for_password()


if __name__ == '__main__':
    # sockets()
    use_sockets()
