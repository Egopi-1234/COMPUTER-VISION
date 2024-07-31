import cv2
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
if eye_cascade.empty():
    print("Error loading eye cascade file")
    exit()
img = cv2.imread(r"C:\image\tv.jpg")
if img is None:
    print("Error loading image")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20))
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Eyes Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
