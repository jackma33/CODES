import os
import textwrap
from PIL import Image
from bg.bg import get_bg
from PIL import ImageFont
from PIL import ImageDraw


def post(image):
    pass


def create(number, quote, by):
    image_path = get_bg()
    img = Image.open(image_path)  # .convert('RGB')
    W, H = img.size

    draw = ImageDraw.Draw(img)

    fonts = [
        'BebasNeue-Regular.ttf',
        'BebasNeue-Regular.ttf',
        'GreatVibes-Regular.ttf'
    ]

    text = f"""{quote}"""
    text = textwrap.fill(text=text, width=25)

    text1 = f"{by}"
    text1 = textwrap.fill(text=text1, width=20)

    text2 = f"#{number}"

    font = ImageFont.truetype(f'./Fonts/{fonts[0]}', 100)
    font1 = ImageFont.truetype(f'./Fonts/{fonts[1]}', 100)

    a, b, w, h = draw.textbbox((0.0, 0.0), text, font=font)
    # print(draw.textbbox((0.0, 0.0), text, font=font))
    t = 0
    while h > 700:
        t += 5
        font = ImageFont.truetype(f'./Fonts/{fonts[0]}', 100-t)
        a, b, w, h = draw.textbbox((0.0, 0.0), text, font=font)
        if h < 700:
            break
    a, b, w1, h1 = draw.textbbox((0.0, 0.0), text1, font=font)

    text_color = (250, 250, 250, 250)

    draw.text(((W-w)/2, (H-h)/2-100), text, font=font, fill=text_color)
    draw.text(((W-w1)/2, 1025), text1, font=font, fill=text_color)
    draw.text((425, 85), text2, font=font1, fill=text_color)

    img.save('quote.png')
    try:
        os.rename('./quote.png', './quote.jpg')
    except:
        os.remove('./quote.jpg')
        os.rename('./quote.png', './quote.jpg')


def main():
    file = './data/quotes.txt'

    f = open(file, encoding='UTF8')
    quotes = f.readlines()
    quote = quotes[0].strip('\n')

    quotes.pop(0)
    with open(file, 'w', encoding='UTF8') as f:
        for i in quotes:
            f.write(i)
    f.close()

    with open('./data/done.txt', 'a+', encoding='UTF8') as f:
        f.write(quote)
        f.write('\n')
    f.close()

    Number = quote.split('.')[0].strip()
    By = quote.split('–')[-1].replace('.', '').replace(',', '').strip()
    Quote = quote.replace(Number, '').replace(By, '').replace(
        '. ', '').replace('–', '').replace('.', '').replace(',', ';').strip()
    print(Number, '-', Quote)
    create(Number, Quote, By)
    post('quote.jpg')


if __name__ == '__main__':
    main()
