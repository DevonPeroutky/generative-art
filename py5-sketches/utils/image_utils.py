from typing import Optional

from PIL import Image


class ImageUtils:

    @staticmethod
    def resize_image(og_image: Image, height: Optional[int], width: Optional[int]) -> Image:
        if height is None and width is None:
            raise ValueError("Either height or width must be provided")

        if height is not None and width is not None:
            return og_image.resize((width, height))

        if height is not None:
            aspect_ratio = og_image.width / og_image.height
            new_width = int(height * aspect_ratio)
            return og_image.resize((new_width, height))

        if width is not None:
            aspect_ratio = og_image.height / og_image.width
            new_height = int(width * aspect_ratio)
            return og_image.resize((width, new_height))
