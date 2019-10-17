import sys

from common import clients
from config import logs as log
from config.config import *


def send_to(session_id, message):
    for client in clients:
        if client.session_id == session_id:
            client.send(message.JsonMessage.encode())
            print(log.message_sent + str(session_id))
            break


def send_to_all(message):
    for client in clients:
        client.send(message.JsonMessage.encode())
        print(log.message_sent + "all")
        break


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
            print(log.successful_binding + get_time())
            print(log.address + self.host + ":" + str(self.port))
            self.server.listen()
            print(log.waiting + log.triple_dots)

        except socket.error as error_msg:
            print(log.problem_in_binding + log.triple_dots + log.exiting + "." + get_time())
            print(error_msg)
            self.server = None
            sys.exit(0)
        return self.server
