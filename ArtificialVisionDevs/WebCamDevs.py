import cv2
import numpy as np

class WebCamDevs:
    num_camera = int

    def __init__(self, num_camera):
        self.num_camera = num_camera

    def open_camera(self):
        vid = cv2.VideoCapture(self.num_camera)
        while (True):
            ret, frame = vid.read()
            """hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)"""

            lower_red = np.array([0, 0, 200], dtype="uint8")
            upper_red = np.array([100, 100, 255], dtype="uint8")
            mask_red = cv2.inRange(frame, lower_red, upper_red)
            """mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)"""
            lower_blue = np.array([200, 0, 0], dtype="uint8")
            upper_blue = np.array([255, 100, 100], dtype="uint8")
            mask_blue = cv2.inRange(frame, lower_blue, upper_blue)
            """"mask_blue = cv2.inRange(hsv_frame, lower_blue, upper_blue)"""
            lower_green = np.array([0, 2000, 0], dtype="uint8")
            upper_green = np.array([100, 255, 100], dtype="uint8")
            mask_green = cv2.inRange(frame, lower_green, upper_green)
            """mask_green = cv2.inRange(hsv_frame, lower_green, upper_green)"""
            the_mask = cv2.bitwise_or(mask_red, mask_blue, mask_green)

            detected_output = cv2.bitwise_and(frame, frame, mask=the_mask)

            cv2.imshow('frame', detected_output)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        vid.release()
        cv2.destroyAllWindows()
