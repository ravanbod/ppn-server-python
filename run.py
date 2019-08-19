import sys
import socket
import threading
from config import config as conf
from config import messages as msg


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
run_server(conf.HOST, conf.PORT)

while True:
    if conf.MAX_CLIENT == -1 or len(clients) <= conf.MAX_CLIENT:
        client, address = server.accept()

