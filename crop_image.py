import cv2
img = cv2.imread("lang-hoa-dep-15.jpg")
y = 0
h = 300
x = 0
w = 300
crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)