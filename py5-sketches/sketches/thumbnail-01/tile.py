import random

from PIL import Image

import py5
import py5_tools
from ...utils.image_utils import ImageUtils
from ...models.circle import Circle


w, h = 75, 75
img = Image.open("./py5-sketches/images/reddit-transparent.png")
img = img.resize((w, h), Image.LANCZOS)


def setup():
    py5.size(1440, 1440)
    py5.no_stroke()
    py5.no_loop()


def draw():
    # loop through the width in interval of w
    for i in range(0, 1440, 35):
        for j in range(0, 1440, 35):
            c = py5.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(10, 100))
            # Circle(i, j, radius=random.randint(5, 30), color=c, img=None).display()
            Circle(i, j, radius=random.randint(15, 15), color=None, img=img).display()
            # Circle(i, j, radius=random.randint(5, 30), color=c, img=None).display()


py5.run_sketch()
