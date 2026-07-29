#### Transform the grid in a picture and export it ####

from PIL import Image

def save_png(grid, palette, filename, pixel_size=1):

    image = Image.new("RGB", (grid.width, grid.height))

    for y in range(grid.height):
        for x in range(grid.width):
            color_id = grid.get_pixel(x, y)
            rgb = palette.get_color(color_id)
            image.putpixel((x, y), rgb)

    if pixel_size > 1:
        image = image.resize( (grid.width * pixel_size, grid.height * pixel_size) , Image.Resampling.NEAREST)

    image.save("/home/colin/Pictures/Generated/Test_01/" + filename)