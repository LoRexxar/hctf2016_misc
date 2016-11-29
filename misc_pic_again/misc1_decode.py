# coding: utf-8
from PIL import Image

im = Image.open('flag.png')


width = im.size[0]
height = im.size[1]

a = ""
aa = ""

for y in xrange(height):
	for x in xrange(width):

		pixel = im.getpixel((x, y))

		for i in xrange(3):
			aa += str(pixel[i]%2)

for i in xrange(len(aa)):
	try:
		a += chr(int(aa[i*8:i*8+8],2))
	except:
		break

fflag = open("test.zip","w")

fflag.write(a)
fflag.close()