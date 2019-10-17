# This file contains common variables and functions of project, such as clients list and etc.
import config.logs as log

clients = []


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
