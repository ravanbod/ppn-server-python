import socket

# --- Server Variables START ---
HOST = socket.gethostbyname(socket.gethostname())
PORT = 25088
MAX_CLIENT = 1000  # Set this -1 if you want unlimited clients.
# --- Server Variables END ---
