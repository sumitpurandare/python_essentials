from PIL import Image,ImageFilter

img_4 = Image.open('./pokemon_4.jpg')

img_filter = img_4.convert('L')

#img_filter.save("convert.png",'png')

#crooked = img_filter.rotate(90)
img_filter.resize((100,100))
resized = img_filter.save("resized.png","png")
print(resized.size)