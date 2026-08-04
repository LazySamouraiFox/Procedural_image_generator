#### Main function that execute the pipeline ####

from palette import Palette
from grid import Grid
from exporter import save_png
from passes import PixelRulePass
from rules.clusters import ClusterRules
from rules.borders import BorderRules


WIDTH = 32
HEIGHT = 32

palette = Palette()

grid = Grid(WIDTH, HEIGHT)

grid.random_fill(palette)

pipeline = [PixelRulePass(ClusterRules(range=1).grow_clusters, iterations=7),
            PixelRulePass(ClusterRules(range=3).grow_clusters, iterations=5),]
            #PixelRulePass(BorderRules().outlines)]

for rule in pipeline:
    grid = rule.apply(grid, palette)

save_png(grid,palette,"test_range_growth_clusters.png",pixel_size=8)