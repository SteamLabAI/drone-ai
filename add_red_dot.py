import random
from PIL import Image, ImageDraw
for i in range(10):
    img = Image.open("./zdjecie.jpg")
    img = img.convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    width, height = img.size
    d = random.randint(15, 30)
    x1 = random.randint(0, width - d)
    x2 = x1 + d
    y1 = random.randint(0, height - d)
    y2 = y1 + d
    r = random.randint(225, 255)
    g = random.randint(0, 50)
    b = random.randint(0, 50)
    a = random.randint(100, 200)
    color = (r, g, b, a)
    draw.ellipse([(x1, y1), (x2, y2)], fill=color)

    img = Image.alpha_composite(img, overlay)
    img = img.convert("RGB")

    img.save("./wyjscie" + str(i) + ".jpg")
