import cv2
img = cv2.imread(r"C:\image\thalapathy.jpg")
if img is None:
    raise FileNotFoundError("The image file was not found. Please check the path.")
cv2.imshow('Original', img)
cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)  
sobely = cv2.convertScaleAbs(sobely)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
