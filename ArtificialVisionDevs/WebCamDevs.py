import cv2
import numpy as np

class WebCamDevs:
    num_camera = int

    def __init__(self, num_camera):
        self.num_camera = num_camera

    def open_camera(self):
        vid = cv2.VideoCapture(self.num_camera)
        redCount = 0
        greenCount = 0
        blueCount = 0
        while (True):
            ret, imageFrame = vid.read()
            hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

            lower_red = np.array([136, 87, 111], dtype="uint8")
            upper_red = np.array([180, 255, 255], dtype="uint8")
            mask_red = cv2.inRange(hsvFrame, lower_red, upper_red)
            """mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)"""
            lower_green = np.array([25, 52, 72], dtype="uint8")
            upper_green = np.array([102, 255, 255], dtype="uint8")
            mask_green = cv2.inRange(hsvFrame, lower_green, upper_green)
            """mask_green = cv2.inRange(hsv_frame, lower_green, upper_green)"""
            lower_blue = np.array([94, 80, 2], dtype="uint8")
            upper_blue = np.array([120, 255, 255], dtype="uint8")
            mask_blue = cv2.inRange(hsvFrame, lower_blue, upper_blue)
            """"mask_blue = cv2.inRange(hsv_frame, lower_blue, upper_blue)"""
            # Morphological Transform, Dilation
            # for each color and bitwise_and operator
            # between imageFrame and mask determines
            # to detect only that particular color
            kernal = np.ones((5, 5), "uint8")
            # For red color
            mask_red = cv2.dilate(mask_red, kernal)
            res_red = cv2.bitwise_and(imageFrame, imageFrame, mask=mask_red)
            # For green color
            mask_green = cv2.dilate(mask_green, kernal)
            res_green = cv2.bitwise_and(imageFrame, imageFrame, mask=mask_green)
            # For blue color
            mask_blue = cv2.dilate(mask_blue, kernal)
            res_blue = cv2.bitwise_and(imageFrame, imageFrame, mask=mask_blue)
            # Creating contour to track red color
            contours, hierarchy = cv2.findContours(mask_red,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)

            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    imageFrame = cv2.rectangle(imageFrame, (x, y),
                                               (x + w, y + h),
                                               (0, 0, 255), 2)

                    redCount+=1
                    cv2.putText(imageFrame, "Red Colour", (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                                (0, 0, 255))

            # Creating contour to track green color
            contours, hierarchy = cv2.findContours(mask_green,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)

            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    imageFrame = cv2.rectangle(imageFrame, (x, y),
                                               (x + w, y + h),
                                               (0, 255, 0), 2)

                    greenCount+=1
                    cv2.putText(imageFrame, "Color Verde", (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (0, 255, 0))

            # Creating contour to track blue color
            contours, hierarchy = cv2.findContours(mask_blue,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    imageFrame = cv2.rectangle(imageFrame, (x, y),
                                               (x + w, y + h),
                                               (255, 0, 0), 2)

                    blueCount+=1
                    cv2.putText(imageFrame, "Color Azul", (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (255, 0, 0))

            the_mask = cv2.bitwise_or(mask_red, mask_blue, mask_green)
            detected_output = cv2.bitwise_and(imageFrame, imageFrame, mask=the_mask)
            print("Red Colour count = %s" % (redCount))
            print("Green Colour count = %s" % (greenCount))
            print("Blue Colour count = %s" % (blueCount))

            cv2.imshow('Detection de colores multiple en tiempo real', imageFrame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                vid.release()
                cv2.destroyAllWindows()
                break
