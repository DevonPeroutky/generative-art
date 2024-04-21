import random
import py5_tools
import py5

from PIL import Image
from colour import Color
from ...utils.image_utils import ImageUtils
from ...models.circle import Circle


w, h = 75, 75
img = Image.open("./py5-sketches/images/reddit-transparent.png")
img = img.resize((w, h), Image.LANCZOS)

py5_img = py5.convert_image(img)


def setup():
    py5.size(1440, 1440, py5.P2D)

    global pg
    pg = py5.create_graphics(1440, 1440, py5.P2D)
    pg.no_stroke()
    py5.no_loop()


def draw():

    pg.begin_draw()
    pg.background(255, 255, 255, 255)

    # loop through the width in interval of w
    for i in range(0, 1440, 35):
        for j in range(0, 1440, 35):
            c = py5.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 100)
            Circle(i, j, radius=random.randint(15, 15), color=None, img=py5_img).display(graphics_override_context=pg)

    pg.end_draw()
    py5.image(pg, 0, 0)
    pg.save(filename="./py5-sketches/sketches/thumbnail-01/outputs/bug.png", drop_alpha=False)


py5.run_sketch()