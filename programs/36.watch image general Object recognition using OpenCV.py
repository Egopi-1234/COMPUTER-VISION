import cv2
watch_cascade = cv2.CascadeClassifier(r"C:\image\watch-cascade.xml")
if watch_cascade.empty():
    print("Error loading watch cascade file")
    exit()
img = cv2.imread(r"C:\image\watch.jpeg")
if img is None:
    print("Error loading image")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
watches = watch_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
if len(watches) == 0:
    print("No watches detected")
else:
    print(f"Detected {len(watches)} watches")
for (x, y, w, h) in watches:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Watches Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
