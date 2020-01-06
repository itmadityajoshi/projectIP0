from PIL import Image, ImageDraw as ig_draw

img = Image.open('apple.jpg').convert("LA")
img.show()

pixels = img.load()
for i in range (img.size[0]):
    for j in range(img.size[1]):
        x,y = pixels[i,j][0],pixels[i,j][1]
        x,y = abs(x-225), abs(y-225)
        pixels[i,j] = x,y

img_draw = ig_draw.Draw(img)
img_draw.text((20,20),"Aditya Joshi",fill='Black')
img.show()
img.save('color_inversion.jpg')
