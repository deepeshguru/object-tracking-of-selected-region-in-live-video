# -*- coding: utf-8 -*-
"""

@author: Deepesh Agrawal
"""


import cv2
import numpy as np
cap = cv2.VideoCapture(0)
ret,frame = cap.read()
flag = True


def run_main(a, frame1):
    c,r,w,h = a[0], a[1], a[2], a[3]
    track_window = (c,r,w,h)
    # Create mask and normalized histogram (dpsh)
    roi = frame1[r:r+h, c:c+w]
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_roi, np.array((0., 30.,32.)), np.array((180.,255.,255.)))
    roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 80, 1)
    
    while True:
        ret, frame1 = cap.read()
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        x,y,w,h = track_window
        cv2.rectangle(frame1, (x,y), (x+w,y+h), 255, 2)
        cv2.imshow('Tracking', frame1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

while True:
    ret,frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('b'):
        a = cv2.selectROI(frame)
        cv2.destroyAllWindows()
        flag = False
    if cv2.waitKey(1) & 0xFF == ord('c') and flag == False:
        print("ok")
        flag = True
        run_main(a, frame) 
        cv2.destroyAllWindows()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 
