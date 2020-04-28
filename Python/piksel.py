from PIL import Image
image = Image.open('test.png')
image.putpixel((0,0), (0.5,0.7,0.3))
print(image.getpixel((0,0)))
