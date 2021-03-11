import cv2
import numpy as np


def detect_red(hsv_frame):
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    return red


def detect_blue(hsv_frame):
    low_blue = np.array(([94, 80, 2]))
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    return blue


def detect_green(hsv_frame):
    low_green = np.array(([94, 80, 2]))
    high_green = np.array([126, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    return green

def detect_rgb(hsv_frame):
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    return result


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    red = detect_red(hsv_frame)
    blue = detect_blue(hsv_frame)
    green = detect_green(hsv_frame)
    result = detect_rgb(hsv_frame)
    cv2.imshow("Main Frame", frame)
    cv2.imshow("Red Color", red)
    cv2.imshow("Blue Color", blue)
    cv2.imshow("Green Color", green)
    cv2.imshow("Result Color", result)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
