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

            lower_red = np.array([0, 0, 200], dtype="uint8")
            upper_red = np.array([100, 100, 255], dtype="uint8")

            mask = cv2.inRange(frame, lower_red, upper_red)

            detected_output = cv2.bitwise_and(frame, frame, mask=mask)

            cv2.imshow('frame', detected_output)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        vid.release()
        cv2.destroyAllWindows()
