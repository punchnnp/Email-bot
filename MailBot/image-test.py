
from PIL import Image, ImageDraw, ImageFont

name = "Nunnapat Kriengchaiyaprug"
text_y_position = 700
img = Image.open('certificate.png')
image_width = img.width
image_height = img.height
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('PinyonScript-Regular.ttf', 100)
text_width, _ = draw.textsize(name, font=font)
draw.text(((image_width - text_width) / 2, text_y_position), name, font=font, fill=(0, 0, 0))
img.save("{}.png".format(name))

img.show("{}.png".format(name))


