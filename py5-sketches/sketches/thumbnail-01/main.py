from PIL import Image

import py5
import py5_tools
from ...utils.image_utils import ImageUtils


w, h = 1280, 720
img = Image.open("./py5-sketches/images/film-portrait.jpg")
portait_img = ImageUtils.resize_image(img, h, None)

print(f'Resized ' + str(img.size) + ' to ' + str(portait_img.size))


def setup():
    py5.size(w, h)
    py5.background(64)
    # py5-sketches.image_mode(py5-sketches.CENTER)

    img = py5.convert_image(portait_img)
    # max of two values
    py5.image(img, max((w - portait_img.width) / 2, 0), 0)


def draw():
    pass

print(py5)

py5.run_sketch()