import cv2 as cv
img = cv.imread("Photos/manzoor.jpg")
img = cv.resize(img,(300,300)) # resizing image
blur_image = cv.GaussianBlur(img,(5,5),0) # blurring image

cv.imshow("Image",img)
cv.imshow("Blur",blur_image)
cv.waitKey(0)
cv.destroyAllWindows()