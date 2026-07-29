#### Main function that execute the pipeline ####

from palette import Palette
from grid import Grid
from exporter import save_png


WIDTH = 32
HEIGHT = 32

palette = Palette()

grid = Grid(WIDTH, HEIGHT)

grid.random_fill(palette)

save_png(grid,palette,"test.png",pixel_size=8)