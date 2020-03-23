import cv2
import socket
import pickle
import struct

HOST = '127.0.0.1'
PORT = 5555

cap = cv2.VideoCapture('input.mp4')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), PORT))

while True:

    ret, frame = cap.read()
    data = pickle.dumps(frame)
    client_socket.sendall(struct.pack('L', len(data) + data))

    if frame == False:
        break

client_socket.close()