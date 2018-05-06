from PIL import Image
import PIL.ImageOps


for i in range(1,1001):
	image = Image.open(str(i) + '.png')

	inverted_image = PIL.ImageOps.invert(image)

	inverted_image.save(str(i) + '.png')
