import cv2
import socket
import numpy as np

HOST = '127.0.0.1'
PORT = 5555

cap = cv2.VideoCapture(0)

cap.set(3, 320)
cap.set(4, 240)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), PORT))

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY)]

while True:

    ret, frame = cap.read()

    result, frame = cv2.imencode('.jpg', frame, encode_param)

    data = np.array(frame)
    stringData = data.tostring()

    client_socket.sendall((str(len(stringData))).encode().ljust(16) + stringData)


client_socket.close()