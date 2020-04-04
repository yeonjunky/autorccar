import socket
import cv2
import numpy as np

import cv2
import numpy as np

def apply_canny(img):
    img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
    Gblur = cv2.GaussianBlur(img, (5, 5), 0)
    canny = cv2.Canny(Gblur, 50, 150)
    return canny

def apply_segment(img):
    height_top = img.shape[1]
    width = img.shape[1]
    polygons = np.array([
        [(0, 0), (width, 0), (width, 10),(0, 10)]
    ])
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, polygons, 255)
    segment = cv2.bitwise_and(img, mask)
    return segment

def line_detection(frame):

    while True:
        frame = cv2.resize(frame, (640, 360))
        canny = apply_canny(frame)
        seg = apply_segment(canny)
        seg2 = apply_segment(frame)
        linesP = cv2.HoughLinesP(seg, 1, np.pi / 180, 100, np.array([]), minLineLength = 100, maxLineGap = 50)

        if linesP is not None:
            for i in range(0, len(linesP)):
                l = linesP[i][0]
                cv2.line(seg, (l[0], l[1]), (l[2], l[3]), (255, 255, 255), 3, cv2.LINE_AA)

        cv2.imshow('cap', seg)
        cv2.imshow('vid', seg2)

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
    # line_detection(frame)
    if cv2.waitKey(1) == ord('q'):
        break



server_socket.close()
