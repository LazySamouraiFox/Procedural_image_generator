#### Grid manager ####

from numpy import zeros as np_zeros
from numpy import full as np_full
from numpy import unique as np_unique
from numpy.random import choice as np_choice
from random import randrange as rd_randrange

class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = np_full((height, width), None)

    def get_pixel(self, x, y):
        return self.pixels[y][x]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color
        
    def in_bounds(self, x, y):
        return (0 <= x < self.width and 0 <= y < self.height)
        
    def get_neighbors(self, x, y, radius=1):
        """        
        The center [radius][radius] corresponds to (x, y) itself.
        Index [radius + dy][radius + dx] gives the pixel at (x+dx, y+dy).
        Out of bounds positions are None.
        """
        size = 2 * radius + 1
        neighbors = np_full((size, size), None)
        
        for dy in range(-radius, radius + 1):
            for dx in range(-radius, radius + 1):
                nx, ny = x + dx, y + dy
                if self.in_bounds(nx, ny):
                    neighbors[radius + dy][radius + dx] = self.pixels[ny][nx]
                    
        return neighbors

    def random_fill(self, palette):
        for y in range(self.height):
            for x in range(self.width):
                color_id = rd_randrange(palette.size())    #randrange(start(default=0), stop[, step])
                self.set_pixel(x, y, color_id)

    def clone(self):
        new_grid = Grid(self.width, self.height)
        for y in range(self.height):
            for x in range(self.width):
                new_grid.set_pixel(x, y, self.get_pixel(x, y))
        return new_grid

    def count_neighbors(self, x, y, color, radius=1):
        
        neighbors = self.get_neighbors(x, y, radius)
        c=0
        
        for current_color in neighbors:
            if current_color==color:
                c+=1
        
        return c
    
    def majority_color(self, x, y, palette, radius=1):
        """
        returns a list of the majority colors among the neighbors within the radius.
        if there are colors that has the same number of occurences, it returns a list.
        """        
        
        neighbors = self.get_neighbors(x, y, radius)
        neighbors_color = np_zeros(palette.size())
        
        for current_color in neighbors:
            neighbors_color[current_color]+=1
        
        values, counts = np_unique(neighbors_color, return_counts=True)
        most_frequent_values = values[counts == counts.max()]
        
        return most_frequent_values

    def random_neighbor(self, x, y, radius=1):
        neighbors=self.get_neighbors(x, y, radius)
        return np_choice(neighbors)
