from PIL import Image 
import numpy as np 
pic = Image.open('apple.jpg')
pic.show('apple.jpg')
img = Image.open('apple.jpg').convert('L')
img.show('greyscale.jpg')
pic_array = np.array(img)
print(pic_array)
print(img_array)
