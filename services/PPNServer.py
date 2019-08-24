import socket
import sys

from config import messages as msg


class PPNServer:
    server = None
    host = None
    port = None

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host, self.port))
            print(msg.successful_binding)
            print(msg.address + self.host + ":" + str(self.port))
            self.server.listen()
            print(msg.waiting + msg.triple_dots)

        except socket.error as error_msg:
            print(msg.problem_in_binding + msg.triple_dots + msg.exiting)
            print(error_msg)
            self.server = None
            sys.exit(0)
        return self.server
