import cv2
path = r"C:\image\thalapathy.jpg"
src = cv2.imread(path)
if src is None:
    print("Error: Image not found at", path)
else:
    rotated_image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
    rotated_image = cv2.rotate(rotated_image, cv2.ROTATE_90_CLOCKWISE)
    rotated_image = cv2.rotate(rotated_image, cv2.ROTATE_90_CLOCKWISE)
    
    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
