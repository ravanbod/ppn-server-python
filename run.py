import os

from models.Client import *
from services.PPNServer import *


def get_input():
    global server
    while True:
        s = input()
        if s == "exit":
            print(log.server_closed + get_time())
            server.close()
            os._exit(1)
            break


server = PPNServer(HOST, PORT).run()  # Run PPN Server
if __name__ == "__main__" and server is not None:
    threading.Thread(target=get_input, args=[]).start()
    while True:
        if MAX_CLIENT == -1 or len(com_vars.clients) <= MAX_CLIENT:
            c, a = server.accept()  # A new client connected.
            session_id = c.recv(1024).decode()  # First sent message from client is session_id
            com_vars.clients.append(Client(c, a, session_id))  # Add new client to clients list.
        else:  # Max clients reached
            print(logs.max_client + logs.triple_dots + "." + get_time())
