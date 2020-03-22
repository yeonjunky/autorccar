import numpy as np
import cv2
from pyautogui import screenshot
from PIL import ImageGrab
from PIL import Image

class collect_traning_data():

    def capture_image(self):
        cnt = 1
        while True:
            img = ImageGrab.grab()
            img.show()
            if cv2.waitKey(0) == ord("k"):
                img.close()
                file_name = "data_image\{}.jpg".format(cnt)
                img.save(file_name)
                cnt += 1

            elif cv2.waitKey(0) == ord("q"):
                break

    def image_processing(self):
        cnt = 1
        img = cv2.imread('data_image/data%d.jpg' % cnt, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)


a = collect_traning_data()
a.capture_image()