import cv2
path = r"C:\image\thalapathy.jpg"
src = cv2.imread(path)
if src is None:
    print(f'Error: Image not loaded from {path}')
else:
    window_name = 'Image'
    image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
