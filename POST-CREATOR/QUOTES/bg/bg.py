import os
from PIL import Image
import requests
from random import randint

"""
https://www.pexels.com/api/documentation/?
"""

def get_image():
    headers = {
        'Authorization': "563492ad6f917000010000016fd21ba26fff41618ae1be07284cdda0"
    }

    param = {
        "query": "abstract",
        "orientation": "portrait",
        "page": str(randint(1, 25))
    }

    r = requests.get("https://api.pexels.com/v1/search",
                    headers=headers, params=param)
    # print(r.headers['X-Ratelimit-Remaining'])

    while 1:
        try:
            img_url = r.json()['photos'][randint(1, 25)]['src']['medium']
            break
        except:
            continue

    r1 = requests.get(img_url)
    with open('./bg/pic.jpg', 'wb') as f:
        f.write(r1.content)

def apply_overlay():
    Overlay = "./bg/Black_overlay.jpg"
    Apply_2_Image = "./bg/pic.jpg"

    # fg = Image.open('/content/overlay.jpg').convert('RGB')
    fg = Image.open(str(Overlay)).convert('RGB')
    bg = Image.open(str(Apply_2_Image)).convert('RGB')
    bg = bg.resize((1080, 1350))
    # bg = Image.open(str(Apply_2_Image)).convert('RGB')

    w, h = bg.width, bg.height

    im = fg.resize((w, h))
    im.save('./bg/overlay_resized.jpg', 'png')
    fg = Image.open('./bg/overlay_resized.jpg').convert('RGB')
    # set alpha to .7
    Image.blend(bg, fg, .69).save("./bg/image.jpg")

def apply_template():
    # import PIL module
    from PIL import Image
    filename = './bg/Quote_template.png'
    filename1 = './bg/image.jpg'
    frontImage = Image.open(filename)
    background = Image.open(filename1)
    frontImage = frontImage.convert("RGBA")
    background = background.convert("RGBA")
    width = (background.width - frontImage.width) // 2
    height = (background.height - frontImage.height) // 2
    background.paste(frontImage, (width, height), frontImage)
    background.save("./bg/Quote.png", format="png")
    # os.rename("./bg/Quote.png", "./bg/Quote.jpg")


def get_bg():
    get_image()
    apply_overlay()
    apply_template()
    return "./bg/Quote.png"

if __name__== '__main__':
    get_bg()
