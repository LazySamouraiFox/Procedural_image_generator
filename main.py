#### Main function that execute the pipeline ####

from palette import Palette
from grid import Grid
from exporter import save_png
from passes import RulePass
from rules.clusters import ClusterRules


WIDTH = 32
HEIGHT = 32

palette = Palette()

grid = Grid(WIDTH, HEIGHT)

grid.random_fill(palette)

pipeline = [RulePass(ClusterRules().plus_clusters, iterations=5),
            RulePass(ClusterRules().multiply_clusters, iterations=5)]

for rule in pipeline:
    grid = rule.apply(grid)

save_png(grid,palette,"test.png",pixel_size=8)