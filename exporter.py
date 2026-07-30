#### Transform the grid in a picture and export it ####

from PIL import Image
from pathlib import Path

OUTPUT_FOLDER = Path("/home/colin/Pictures/Generated/Test_01/")
OUTPUT_FOLDER.mkdir(exist_ok=True)

def save_png(grid, palette, filename, pixel_size=1):

    image = Image.new("RGB", (grid.width, grid.height))

    for y in range(grid.height):
        for x in range(grid.width):
            color_id = grid.get_pixel(x, y)
            rgb = palette.get_color(color_id)
            image.putpixel((x, y), tuple(rgb))

    if pixel_size > 1:
        image = image.resize( (grid.width * pixel_size, grid.height * pixel_size) , Image.Resampling.NEAREST)

    image.save(OUTPUT_FOLDER / filename)
    # image.save("C:/Colin/Scripts/Procedural_image_generator/Images/Test_01/" + filename)