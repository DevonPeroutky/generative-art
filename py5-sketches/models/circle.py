import py5
import py5_tools

from typing import Optional
from PIL import Image


class Circle:
    def __init__(self, x: int, y: int, radius: int, color, img: Optional[Image.Image]):
        self.x = x
        self.y = y
        self.radius = radius

        assert color is not None or img is not None, "Either color or img must be provided"
        self.color = color
        self.img = img

    def intersects(self, other: "Circle") -> bool:
        d = py5.dist(self.x, self.y, other.x, other.y)
        return d < other.radius

    def will_intersect(self, other: "Circle") -> bool:
        d = py5.dist(self.x, self.y, other.x, other.y)
        return d < self.radius + other.radius

    def display(self, graphics_override_context=None):
        if self.color is not None:
            if graphics_override_context is not None:
                graphics_override_context.fill(self.color)
                graphics_override_context.ellipse(self.x, self.y, self.radius * 2, self.radius * 2)
            else:
                py5.fill(self.color)
                py5.ellipse(self.x, self.y, self.radius * 2, self.radius * 2)
        else:
            if graphics_override_context is not None:
                graphics_override_context.image(self.img, self.x, self.y, self.radius * 2, self.radius * 2)
            else:
                py5.image(self.img, self.x, self.y, self.radius * 2, self.radius * 2)