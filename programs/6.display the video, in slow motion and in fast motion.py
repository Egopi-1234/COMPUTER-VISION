import cv2
cap = cv2.VideoCapture("C:\\image\\vijay video.mp4")
if not cap.isOpened():
    print("Error opening video file")
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
