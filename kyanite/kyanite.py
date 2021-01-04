from typing import Tuple

from PIL import Image


TR_MODES = {
    "RGB": (255, 255, 255)
}


def get_transparency(mode: str) -> Tuple(int):
    return TR_MODES[mode.upper()]


def compose_watermark(image: str, watermark: str, pos_x: int, pos_y: int, transparency: int = 0):
    with Image.open(image, "r") as img:
        # img_w, img_h = img.size  # Need for testing purposes.
        with Image.open(watermark, "r") as wm:
            result = Image.new("RGB", img.size, get_transparency("RGB"))
            result.paste(img, (0, 0))
            result.paste(wm, (pos_x, pos_y))
            result.save("out.png")


# Write argparser.
compose_watermark("background.png", "watermark.png", 20, 20)
