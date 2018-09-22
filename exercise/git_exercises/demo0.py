#将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
from PIL import Image, ImageDraw, ImageFont

if __name__ == "__main__":
    im = Image.open(r"f:/images/zongzi.png")
    # im.show()

    font = ImageFont.truetype(r"f:/font/demo1.ttf", 96)
    draw = ImageDraw.Draw(im)
    draw.text((im.size[0] - font.size, 0), "4", (256, 0, 0), font=font)
    im.show()