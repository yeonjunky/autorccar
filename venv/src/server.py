import socket
import pickle
import cv2
import struct

PORT = 5555


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((socket.gethostname(), PORT))

server_socket.listen()

client_socket, addr = server_socket.accept()

print('connected by', addr)

while True:

    data = client_socket.recv(4096)

    if not data:
        break

    frame = pickle.loads(data)


server_socket.close()
