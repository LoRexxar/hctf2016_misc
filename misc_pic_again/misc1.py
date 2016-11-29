# coding: utf-8
from PIL import Image


fflag = open("justastart.zip","rb")
flag = []

while True:
	byte = fflag.read(1)
	if byte == "":
		break
	else:
		hexstr = "%s" % byte.encode("hex")
		decnum = int(hexstr, 16)
		binnum = bin(int(hexstr, 16))[2:].zfill(8)

		for i in xrange(8):
			flag.append(binnum[i:i+1])

flag.reverse()

im = Image.open('misc1.jpg')


width = im.size[0]
height = im.size[1]

pic = Image.new("RGB",im.size)

for y in xrange(height):
	for x in xrange(width):

		pixel = list(im.getpixel((x, y)))

		for i in xrange(3):
			count = pixel[i]%2

			if len(flag) == 0:
				break

			if count == int(flag.pop()):
				continue

			if count == 0:
				pixel[i]+=1

			elif count == 1:
				pixel[i]-=1

		pic.putpixel([x, y],tuple(pixel))

pic.save("flag.png")
