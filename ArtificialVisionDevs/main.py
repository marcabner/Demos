import cv2
import numpy as np
from WebCamDevs import WebCamDevs

if __name__ == '__main__':

    real_time = WebCamDevs(0).open_camera()

    """image = cv2.imread('OpenCV_Logo.jpg')
    lower_red = np.array([0, 0, 200], dtype="uint8")
    upper_red = np.array([0, 100, 255], dtype="uint8")

    mask = cv2.inRange(image, lower_red, upper_red)

    detected_output = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("red color detection", image)

    cv2.waitKey(0)"""





