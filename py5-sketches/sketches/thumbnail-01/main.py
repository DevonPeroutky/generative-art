from PIL import Image

import py5
import py5_tools
from ...utils.image_utils import ImageUtils


w, h = 1280, 720
global portrait_img
portrait_img = ImageUtils.resize_image(Image.open("./py5-sketches/images/film-portrait.jpg"), h, None)


def setup():
    py5.size(portrait_img.width * 2, portrait_img.height)
    py5.background(255, 255, 255)
    py5.no_stroke()
    # py5.no_loop()

    global img
    img = py5.convert_image(portrait_img)
    img.load_pixels()

    py5.image(img, portrait_img.width, 0)


def draw():
    tiles = max(1, py5.mouse_x // 10)
    # tiles = 10
    tile_size = int(portrait_img.width / tiles)
    print(tiles)
    print(tile_size)

    py5.translate(tile_size / 2, tile_size / 2)

    py5.background(255, 255, 255)
    for x in range(0, portrait_img.width, tile_size):
        for y in range(0, py5.height, tile_size):
            c = img.get_pixels(int(x), int(y))
            py5.fill(c)
            py5.ellipse(x, y, 20, 20)

    print("DONE")

py5.run_sketch()