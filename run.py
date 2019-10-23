import os
import threading

import common
import config.logs as log
from config.config import *
from models.Client import Client
from models.Message import Message
from services.PPNServer import PPNServer, send_to, send_to_all


def get_input():
    global server
    while True:
        s = input()
        if s == "exit":
            print(log.server_closed + get_time())
            server.close()
            os._exit(1)
            break
        elif s == "send":  # This cmd is just for test
            sid = input("session_id?")
            title = input("title?")
            content = input("content?")
            img_url = input("img_url?")
            send_to(sid, Message(title, content, img_url))
        elif s == "send2all":
            title = input("title?")
            content = input("content?")
            img_url = input("img_url?")
            send_to_all(Message(title, content, img_url))

server = PPNServer(HOST, PORT).run()  # Run PPN Server
if __name__ == "__main__" and server is not None:
    threading.Thread(target=get_input, args=[]).start()
    while True:
        if MAX_CLIENT == -1 or len(common.clients) <= MAX_CLIENT:
            c, a = server.accept()  # A new client connected.
            session_id = c.recv(1024).decode()  # First sent message from client is session_id
            common.clients.append(Client(c, a, session_id))  # Add new client to clients list.
        else:  # Max clients reached
            print(log.max_client + log.triple_dots + "." + get_time())
