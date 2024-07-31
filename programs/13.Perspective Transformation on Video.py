import cv2
import numpy as np
cap = cv2.VideoCapture(r"C:\image\vijay video.mp4")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    pts1 = np.float32([[200, 300], [5, 2], [0, 4], [6, 0]])
    pts2 = np.float32([[0, 0], [400, 0], [0, 300], [400, 300]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    height, width = frame.shape[:2]
    result = cv2.warpPerspective(frame, matrix, (width, height))
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Transformed Frame', result)
    if cv2.waitKey(24) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
