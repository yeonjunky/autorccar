import socket
import cv2
import numpy as np

def recv(socket, count):
    buf = b''
    while count:
        newbuf = socket.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf

PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((socket.gethostname(), PORT))

server_socket.listen()

client_socket, addr = server_socket.accept()

print('connected by', addr)

while True:

    length = recv(client_socket, 16)
    stringData = recv(client_socket, int(length))
    data = np.fromstring(stringData, dtype='uint8')

    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
    cv2.imshow('image', frame)
    if cv2.waitKey(1) == ord('q'):
        break



server_socket.close()
