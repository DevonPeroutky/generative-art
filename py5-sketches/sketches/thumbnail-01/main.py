from PIL import Image

import py5
import py5_tools
from ...utils.image_utils import ImageUtils


w, h = 1280, 720
global portrait_img
portrait_img = ImageUtils.resize_image(Image.open("./py5-sketches/images/dr-phil.jpeg"), h, None)

global reddit_logo
reddit_img = ImageUtils.resize_image(Image.open("./py5-sketches/images/reddit-transparent.png"), 25, None)
reddit_logo = py5.convert_image(reddit_img)


def setup():
    py5.size(portrait_img.width * 2, portrait_img.height)
    py5.background(255, 255, 255)
    py5.no_stroke()

    global img
    img = py5.convert_image(portrait_img)
    img.load_pixels()

    reddit_logo.load_pixels()


def draw():
    tiles = max(1, py5.mouse_x // 20)
    tile_size = int(portrait_img.width / tiles)

    py5.fill(255, 255, 255)
    py5.rect(0, 0, portrait_img.width, portrait_img.height)
    py5.image(img, portrait_img.width, 0)

    for x in range(0, portrait_img.width, tile_size):
        for y in range(0, py5.height, tile_size):
            c = img.get_pixels(int(x), int(y))
            py5.fill(c)

            size = py5.remap(py5.brightness(c), 0, 255, tile_size, 5)
            py5.tint(c)
            py5.image(reddit_logo, x, y, size, size)

    print("Done")

py5.run_sketch()