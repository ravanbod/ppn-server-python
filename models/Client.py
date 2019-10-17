import threading

import common
from config import logs as log
from config.config import *
from models.Message import *


class Client:
    client = None
    address = None
    session_id = None

    # You can add any variable which you want here

    def __init__(self, c, addr, session_id):
        self.client = c
        self.address = addr
        self.session_id = session_id
        print(log.new_connection + str(addr) + "-session_id:" + session_id + " ." + get_time())
        threading.Thread(target=self.run, args=[]).start()

    def run(self):
        while True:
            try:
                data = self.client.recv(1024)  # This message is sent from client
                if not data:
                    self.client.close()
                else:
                    print(log.new_message + str(
                        self.address) + "-session_id:" + self.session_id + " -message:" + data.decode())
                    common.send_to_all(Message("title", "con", "url"))
            except socket.error as error_msg:
                self.client.close()
                for index, x in enumerate(common.clients):
                    if x.address == self.address:
                        common.clients.pop(index)
                print(log.close_connection + str(self.address) + "." + get_time())
                break

    def send(self, data):
        self.client.send(data)  # This syntax sends msg to client
