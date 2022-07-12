import pystray
from PIL import Image, ImageDraw


def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image


image = create_image(64, 64, 'black', 'red')
# image = Image.open("C:/NAABO/Codes/z.Official_test/icon.png")


def hello(icon, item):
    print("HELLO")


def exit(icon, item):
    icon.stop()


icon = pystray.Icon("NAABO", image, menu=pystray.Menu(
    pystray.MenuItem("Say HELLO", hello),
    pystray.MenuItem("SubMenu", pystray.Menu(
        pystray.MenuItem("One", hello),
        pystray.MenuItem("Two", hello))),
    pystray.MenuItem("Exit", exit)
))

icon.run()
