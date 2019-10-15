from models.Client import *
from services.PPNServer import *

server = PPNServer(HOST, PORT).run()  # Run PPN Server

if __name__ == "__main__" and server is not None:

    while True:
        if MAX_CLIENT == -1 or len(com_vars.clients) <= MAX_CLIENT:
            c, a = server.accept()  # A new client connected.
            com_vars.clients.append(Client(c, a))  # Add new client to clients list.
        else:  # Max clients reached
            print(logs.max_client + logs.triple_dots + "." + get_time())
