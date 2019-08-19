import sys
import socket
import threading
from config import config as conf
from config import messages as msg


class Client:
    client = None
    address = None
    id = None

    # You can add any variable which you want here

    def __init__(self, c, addr):
        self.client = c
        self.address = addr
        print(msg.new_connection + str(addr))
        threading.Thread(target=self.run, args=[]).start()

    def run(self):
        while True:
            try:
                data = self.client.recv(1024)  # This message is sent from client
                if not data:
                    self.client.close()
                else:
                    print(data.decode())
                    for x in clients:
                        x.send(data)
            except socket.error as error_msg:
                self.client.close()
                for index, x in enumerate(clients):
                    if x.address == self.address:
                        clients.pop(index)
                print(msg.close_connection + str(self.address))
                break

    def send(self, data):
        self.client.send(data)  # this syntax sends msg to client


def run_server(host, port):
    global server
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        print(msg.successful_binding)
        print(msg.host + host)
        print(msg.port + str(port))
        server.listen()
        print(msg.waiting + msg.triple_dots)

    except socket.error as error_msg:
        print(msg.problem_in_binding + msg.triple_dots)
        print(msg.exiting + msg.triple_dots)
        print(error_msg)
        sys.exit(0)


server = None
clients = []

if __name__ == "__main__":
    run_server(conf.HOST, conf.PORT)

    while True:
        if conf.MAX_CLIENT == -1 or len(clients) <= conf.MAX_CLIENT:
            c, a = server.accept()  # A new client connected.
            clients.append(Client(c, a))  # Add new client to clients list.
        else:
            print(msg.max_client + msg.triple_dots)
