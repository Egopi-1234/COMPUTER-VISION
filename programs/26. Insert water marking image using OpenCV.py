import cv2
img = cv2.imread(r"C:\image\thalapathy.jpg")
wm = cv2.imread(r"C:\image\thalapathy1.jpg")
if img is None:
    print("Error: Could not open or find the image.")
    exit()
if wm is None:
    print("Error: Could not open or find the watermark image.")
    exit()
h_wm, w_wm = wm.shape[:2]
h_img, w_img = img.shape[:2]
center_x = int(w_img / 2)
center_y = int(h_img / 2)
top_y = max(center_y - int(h_wm / 2), 0)
left_x = max(center_x - int(w_wm / 2), 0)
bottom_y = min(top_y + h_wm, h_img)
right_x = min(left_x + w_wm, w_img)
wm_resized = cv2.resize(wm, (right_x - left_x, bottom_y - top_y))
roi = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(roi.astype(float), 1, wm_resized.astype(float), 0.3, 0)
img[top_y:bottom_y, left_x:right_x] = result.astype('uint8')
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
