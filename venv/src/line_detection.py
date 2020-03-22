import cv2
import numpy as np

def apply_canny(img):
    img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
    Gblur = cv2.GaussianBlur(img, (5, 5), 0)
    canny = cv2.Canny(Gblur, 50, 150)
    return canny

def apply_segment(img):
    height = img.shape[0]
    width = img.shape[1]
    polygons = np.array([
        [(0, height), (width, height), (width, 260),(0, 260)]
    ])
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, polygons, 255)
    segment = cv2.bitwise_and(img, mask)
    return segment

def line_decetion(video_path):
    cap = cv2.VideoCapture(video_path)

    while (cap.isOpened()):
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 360))
        canny = apply_canny(frame)
        seg = apply_segment(canny)
        linesP = cv2.HoughLinesP(seg, 1, np.pi / 180, 100, np.array([]), minLineLength = 100, maxLineGap = 50)

        if linesP is not None:
            for i in range(0, len(linesP)):
                l = linesP[i][0]
                cv2.line(seg, (l[0], l[1]), (l[2], l[3]), (255, 255, 255), 3, cv2.LINE_AA)

        cv2.imshow('cap', seg)

        if cv2.waitKey(33) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

line_decetion('input.mp4')
