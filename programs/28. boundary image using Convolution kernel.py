import cv2
import numpy as np
img = cv2.imread(r"C:\image\thalapathy.jpg", cv2.IMREAD_GRAYSCALE)
dx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
dy = cv2.Sobel(img, cv2.CV_64F, 0, 1)
edges = cv2.magnitude(dx, dy)
edges = np.uint8(cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX))
thresh = 100
_, edges = cv2.threshold(edges, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
