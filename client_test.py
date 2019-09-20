import json
import socket  # Import socket module
import threading

import config.config as config


def get_input():
    while True:
        u = {"msg": input(), "lol": True}
        s.send(json.dumps(u).encode())


def get_messages():
    while True:
        print(s.recv(1024).decode())


s = socket.socket()
s.connect((config.HOST, config.PORT))
threading.Thread(target=get_input, args=[]).start()
threading.Thread(target=get_messages, args=[]).start()
