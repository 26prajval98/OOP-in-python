import cv2

# Weighted Images
# img1 = cv2.imread('images/1917x1080_1.jpg', cv2.IMREAD_COLOR)
# img2 = cv2.imread('images/800x600_2.jpg', cv2.IMREAD_COLOR)
# add = cv2.add(img1,img2)
# add = cv2.addWeighted(img1, 1, img2, 1, 5)
# cv2.imshow('add', add)

# Transperant Images
img1 = cv2.imread('images/1917x1080_1.jpg', cv2.IMREAD_COLOR)
imgC = cv2.imread('images/800x600_3.jpg', cv2.IMREAD_COLOR)

width = imgC.shape[0]
height = imgC.shape[1]

img2 = cv2.cvtColor(imgC, cv2.COLOR_BGR2GRAY)

roi = img1[0:width, 0:height]
ret, thresholdImg = cv2.threshold(img2, 200, 255, cv2.THRESH_BINARY_INV)

invThresholdImg = cv2.bitwise_not(thresholdImg)

imgBg = cv2.bitwise_or(roi, roi, mask=invThresholdImg)
imgCat = cv2.bitwise_or(imgC, imgC, mask=thresholdImg)

img1[0:width, 0:height] = cv2.add(imgBg, imgCat)

cv2.imshow('TPIMG', img1)

cv2.waitKey(0)
