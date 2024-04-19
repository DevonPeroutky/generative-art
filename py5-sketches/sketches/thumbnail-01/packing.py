import random
import py5
import py5_tools

from PIL import Image
from typing import Optional, List
from ...utils.image_utils import ImageUtils
from ...models.circle import Circle


def convert_to_grayscale(img, new_luminance=0.5):
    py5.color_mode(py5.HSB, 360, 1.0, 1.0)
    img.load_pixels()  # Load the pixel data for manipulation

    for i in range(len(img.pixels)):
        current_color = img.pixels[i]
        h = py5.hue(current_color)  # Hue value, not used in grayscale conversion
        s = 0  # Set saturation to zero for grayscale
        l = py5.brightness(current_color)  # Use the brightness as luminance
        a = py5.alpha(current_color)  # Keep the alpha channel unchanged

        # Create a new grayscale color with adjusted luminance
        new_color = py5.color(h, s, new_luminance, a)
        img.pixels[i] = new_color  # Set the new color to the pixel

    img.update_pixels()  # Apply the changes to the pixel array


def create_new_circle(circles: List[Circle], x, y, radius, color) -> Optional[Circle]:
    new_circle = Circle(x, y, radius, color, None)
    for circle in circles:
        if new_circle.intersects(circle):
            return None
    return new_circle


def setup():
    py5.size(1159, 676)
    py5.no_stroke()
    py5.no_loop()

    # Setup base image
    global base_img
    base_img = py5.load_image("./py5-sketches/images/dr-phil.jpeg")
    py5.image(base_img, 0, 0)

    # Setup logo image
    global logo_image
    img = Image.open("./py5-sketches/images/reddit-transparent.png").resize((20, 20), Image.LANCZOS)
    logo_image = py5.convert_image(img)


def draw():
    # loop through the width in interval of w
    canvas_w, canvas_h = base_img.width, base_img.height

    circles = []
    for i in range(0, canvas_w, 2):
        for j in range(0, canvas_h, 2):
            pixel = base_img.get_pixels(i, j)
            print(pixel)
            c = py5.color(py5.red(pixel), py5.green(pixel), py5.blue(pixel), py5.alpha(pixel))

            # Pick a random x and y coordinate
            new_circle = create_new_circle(circles, i, j, random.randint(3, 10), c)
            new_circle.display()

    print("Done")


py5.run_sketch()
