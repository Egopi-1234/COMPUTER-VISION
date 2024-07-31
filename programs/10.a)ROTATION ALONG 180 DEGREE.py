import cv2
path = r"C:\image\thalapathy.jpg"
src = cv2.imread(path)
if src is None:
    print(f"Failed to load image at '{path}'")
else:
    window_name = 'Image'
    image = cv2.rotate(src, cv2.ROTATE_180)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
