from cv2 import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

cap.set(3, 500)
cap.set(4, 500)

camera = True
while camera == True :
    _, frame = cap.read()

    for code in decode(frame) :
        data = code.data.decode('utf-8')
        print(data)
        points = np.array([code.polygon], np.int32)
        points = points.reshape((-1, 1, 2))
        cv2.polylines(frame, [points], True, (0, 255, 0), 5)
        points2 = code.rect
        cv2.putText(frame, data, (points2[0], points2[1]), cv2.FONT_HERSHEY_SIMPLEX,
        0.9, (255, 0, 255), 2)

    if cv2.waitKey(1) == ord('q'):
        break

    cv2.imshow('test', frame)
    
