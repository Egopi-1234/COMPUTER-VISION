import cv2
import numpy as np
filename = r"C:\image\thalapathy.jpg"
resized_img = cv2.imread(filename)
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])
resized_wm = cv2.filter2D(resized_img, -1, kernel)
h_img, w_img, _ = resized_img.shape
h_wm, w_wm, _ = resized_wm.shape
center_y = int(h_img / 2)
center_x = int(w_img / 2)
top_y = center_y - int(h_wm / 2)
left_x = center_x - int(w_wm / 2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm
roi = resized_img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0)
resized_img[top_y:bottom_y, left_x:right_x] = result
output_filename = r"C:\image\thalapathy.jpg"
cv2.imwrite(output_filename, resized_img)
cv2.imshow("Sharpened Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
