from PIL import Image, ImageDraw, ImageFont
import random

def randomChr():
    return chr(random.randint(65, 90))

def randomColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def randomColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

if __name__ == "__main__":
    width = 60 * 4
    height = 60
    im = Image.new("RGB", (width, height), (255, 255, 255))

    font = ImageFont.truetype(r"F:\font/demo1.ttf", 36)

    draw = ImageDraw.Draw(im)

    #填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=randomColor())

    for i in range(4):
        draw.text((60 * i + 10, 10), randomChr(), font=font, fill=randomColor2())

    im.show()