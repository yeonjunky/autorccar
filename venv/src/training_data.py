import numpy as np
import cv2
import pyautogui

class collect_traning_data():

    def capture_image(self):
        cnt = 1
        while True:
            img = pyautogui.screenshot()
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            cv2.imshow('sdfa', frame)
            if cv2.waitKey(0) == ord("k"):
                cv2.destroyAllWindows()
                cv2.imwrite("data_image/data%d.jpg" % cnt, frame)
                cnt += 1

            elif cv2.waitKey(0) == ord("q"):
                break

    def image_processing(self):
        cnt = 1
        img = cv2.imread('data_image/data%d.jpg' % cnt, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)


a = collect_traning_data()
a.capture_image()