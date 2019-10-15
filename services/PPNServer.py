import socket
import sys

from config import logs as log
from config import config


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
            print(log.successful_binding + config.get_time())
            print(log.address + self.host + ":" + str(self.port))
            self.server.listen()
            print(log.waiting + log.triple_dots)

        except socket.error as error_msg:
            print(log.problem_in_binding + log.triple_dots + log.exiting + config.get_time())
            print(error_msg)
            self.server = None
            sys.exit(0)
        return self.server
