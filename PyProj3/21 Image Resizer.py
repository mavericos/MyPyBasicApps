"""
install pillow if you havent
import pillow
open up the image we want to resize using python
print the current size of that image
specify the size we wanna change it to
save the new resized image
"""
from PIL import Image

def resize_image(size1, size2):

    image = Image.open('Mitio.jpg')

    print(f'Current size : {image.size}')

    resized_image = image.resize((size1, size2))  # двойни скоби !!!
    resized_image.save('Resized_MITIO' + str(size1) + '.jpeg')

size1 = int(input("Enter Width: "))
size2 = int(input("Enter Length: "))
resize_image(size1, size2)