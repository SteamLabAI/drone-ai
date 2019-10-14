import random
import math
from PIL import Image, ImageDraw

img = Image.open("./img.png")
img = img.convert("RGBA")

overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)
width, height = img.size
d = math.floor(random.random() * 10 + 10)
x1 = math.floor(random.random() * (width - d))
x2 = x1 + d
y1 = math.floor(random.random() * (height - d))
y2 = y1 + d
r = math.floor(random.random() * 200 + 100)
g = math.floor(random.random() * 100 + 50)
b = math.floor(random.random() * 100 + 50)
a = math.floor(random.random() * 100 + 150)
color = (r, g, b, a)
draw.ellipse([(x1, y1), (x2, y2)], fill=color)

img = Image.alpha_composite(img, overlay)

img.save("./img2.png")
