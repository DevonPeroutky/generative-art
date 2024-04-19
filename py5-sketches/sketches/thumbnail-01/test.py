from colour import Color

import py5_tools
import py5


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


def modify_image_hue(img, hue_shift):
    img.load_pixels()  # Load the pixel data for manipulation

    for i in range(len(img.pixels)):
        current_color = img.pixels[i]
        h = (py5.hue(current_color) + hue_shift) % 360  # Calculate new hue, wrap around with modulo 360
        s = py5.saturation(current_color)  # Keep the saturation the same
        b = py5.brightness(current_color)  # Keep the brightness the same
        a = py5.alpha(current_color)  # Keep the alpha the same
        new_color = py5.color(h, s, b, a)  # Create a new color with the adjusted hue
        img.pixels[i] = new_color  # Set the new color to the pixel

    img.update_pixels()  # Apply the changes to the pixel array


def setup():
    py5.size(1440, 1440, py5.P2D)

    global pg
    pg = py5.create_graphics(1440, 1440, py5.P2D)
    pg.no_stroke()
    py5.no_loop()


def draw():
    pg.begin_draw()
    pg.background(0, 0)
    pg.fill(255, 0, 0)
    pg.ellipse(720, 720, 100, 100)

    pg.end_draw()
    py5.image(pg, 0, 0)
    pg.save(filename="./py5-sketches/sketches/thumbnail-01/outputs/bug.png", drop_alpha=False)


py5.run_sketch()