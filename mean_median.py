#   mean filter

import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
image2 = cv2.imread('joker.jpg') # reads the image

image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
figure_size = 9
new_image = cv2.blur(image2,(figure_size, figure_size))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image, cmap='gray'),plt.title('Mean filter')
plt.xticks([]), plt.yticks([])
plt.show()






# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# image = cv2.imread("noisy.jpg", cv2.COLOR_BGR2GRAY)
# cv2.imshow("Input", image)
# image = cv2.meanBlur(image, 5)
# cv2.imshow("Output", image)
# cv2.waitKey(0)