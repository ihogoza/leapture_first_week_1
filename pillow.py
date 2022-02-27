from PIL import Image

# pillow illustration
img = Image.open('/home/ihogoza/Downloads/baby.jpeg')
print()
print('The size of this image is:' + str(img.size))
img.show()
print('The format of this image is:' +img.format)
img.save('/home/ihogoza/Downloads/baby1.png')
img.thumbnail((50, 30))
img.show()
img.rotate(50).show()
gray_img = Image.open('/home/ihogoza/Downloads/baby.jpeg').convert('L')
gray_img.show()

