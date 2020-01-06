from PIL import Image , ImageDraw
import PIL.ImageOps  
image = Image.open('apple.jpg')

inverted_image = PIL.ImageOps.invert(image)
# img_draw = ImageDraw.Draw(inverted_image)
# img_draw.text((50,450),'BIKRAM TWAYANA' , fill ='red' )

inverted_image.save('aa.jpg')





