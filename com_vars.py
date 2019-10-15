# This file contains common variables of project, such as clients list and etc.
clients = []


def send_to(session_id, message):
    for client in clients:
        if client.session_id == session_id:
            client.send(message.JsonMessage)
            break


def send_to_all(message):
    for client in clients:
        client.send(message.JsonMessage.encode())
        break
