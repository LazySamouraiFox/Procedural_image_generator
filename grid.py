#### Grid manager ####

from random import randrange as rd_randrange

class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [ [None for _ in range(width)] for _ in range(height) ]

    def get_pixel(self, x, y):
        return self.pixels[y][x]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color
        
    def in_bounds(self, x, y):
        return (0 <= x < self.width and 0 <= y < self.height)
        
    def get_neighbors(self, x, y):    
        """
        return a list of the neighbors pixels starting from the left pixel going anti trigonometric
        """   
         
        neighbors = [None for i in range(8)]
        if self.in_bounds(x-1, y):
            neighbors[0]=self.pixels[y][x-1]
        if self.in_bounds(x-1, y+1):
            neighbors[1]=self.pixels[y+1][x-1]
        if self.in_bounds(x, y+1):
            neighbors[2]=self.pixels[y+1][x]
        if self.in_bounds(x+1, y+1):
            neighbors[3]=self.pixels[y+1][x+1]
        if self.in_bounds(x+1, y):
            neighbors[4]=self.pixels[y][x+1]
        if self.in_bounds(x+1, y-1):
            neighbors[5]=self.pixels[y-1][x+1]
        if self.in_bounds(x, y-1):
            neighbors[6]=self.pixels[y-1][x]
        if self.in_bounds(x-1, y-1):
            neighbors[7]=self.pixels[y-1][x-1]
        
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
