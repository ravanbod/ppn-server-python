import sys
import socket
import errno
from config import config as conf
from config import messages as msg


def bind_server(host, port):
    global server
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        print(msg.successful_binding)
        print(msg.host + host)
        print(msg.port + str(port))

    except socket.error as error_msg:
        print(msg.problem_in_binding + msg.triple_dots)
        print(msg.exiting + msg.triple_dots)
        print(error_msg)
        sys.exit(0)


server = None
bind_server(conf.host, conf.port)
