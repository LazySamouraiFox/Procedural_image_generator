#### Main function that execute the pipeline ####

from palette import Palette
from grid import Grid
from exporter import save_png
from passes import RulePass
from rules.clusters import plus_sign_clusters, multiply_sign_clusters


WIDTH = 32
HEIGHT = 32

palette = Palette()

grid = Grid(WIDTH, HEIGHT)

grid.random_fill(palette)

pipeline = [RulePass(plus_sign_clusters, iterations=2), RulePass(multiply_sign_clusters, iterations=2)]

for n in pipeline:
    n.apply(grid)

save_png(grid,palette,"test.png",pixel_size=8)