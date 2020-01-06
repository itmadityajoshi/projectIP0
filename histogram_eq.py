
import cv2                                                          Aditya
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("image2.jpg",cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY )
cv2.imshow("Input",image)
plt.subplot(1,2,1),plt.hist(image.ravel(),256,[0,256])
image = cv2.equalizeHist(image)
cv2.imshow("Output",image)
plt.subplot(1,2,2),plt.hist(image.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)