import json
import socket
import threading

import com
from config import logs as log
from config import config


class Client:
    client = None
    address = None
    session_id = None

    # You can add any variable which you want here

    def __init__(self, c, addr):
        self.client = c
        self.address = addr
        print(log.new_connection + str(addr) + "." + config.get_time())
        threading.Thread(target=self.run, args=[]).start()

    def run(self):
        while True:
            try:
                data = self.client.recv(1024)  # This message is sent from client
                if not data:
                    self.client.close()
                else:
                    print(json.loads(data.decode()))  # Convert Json data to an array
                    for x in com.clients:
                        x.send(data)
            except socket.error as error_msg:
                self.client.close()
                for index, x in enumerate(com.clients):
                    if x.address == self.address:
                        com.clients.pop(index)
                print(log.close_connection + str(self.address) + "." + config.get_time())
                break

    def send(self, data):
        self.client.send(data)  # This syntax sends msg to client
