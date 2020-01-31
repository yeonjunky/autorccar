import cv2
import numpy as np
import glob

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30 , 0.001)

objp = np.zeros((8*8, 3), np.float32)
objp[:, :2] = np.mgrid[0:8, 0:8].T.reshape(-1, 2)

obj_points = []
img_points = []

height = 0
width = 0

images = glob.glob('chess_board/chess_img*.jpg')

for board in images:
    img = cv2.imread(board, cv2.IMREAD_GRAYSCALE)

    ret, counters = cv2.findChessboardCorners(img, (8, 8))

    if ret == True:
        td_points.append(objp)

        corners2 = cv2.cornerSubPix(img, corners, (11, 11), (-1, -1), criteria)
        img_points.append(corners2)

        img = cv2.drawChessboardCorners(img, (8, 8), corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, img.shape[::-1], None, None)

data = {'camera_matrix': np.asarray(mtx).tolist(),
        'dist_coeff': np.asarray(dist).tolist()}

with open("calibration.txt", "w") as f:
    f.write(data)