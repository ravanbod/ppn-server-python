import sys

from config import logs
from config.config import *


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
            print(logs.successful_binding + get_time())
            print(logs.address + self.host + ":" + str(self.port))
            self.server.listen()
            print(logs.waiting + logs.triple_dots)

        except socket.error as error_msg:
            print(logs.problem_in_binding + logs.triple_dots + logs.exiting + get_time())
            print(error_msg)
            self.server = None
            sys.exit(0)
        return self.server
