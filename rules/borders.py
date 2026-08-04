#### Border rules ####

class BorderRules:
    
    def outlines(self, x, y, grid, palette):
        
        outline_color = 0   # Let's say the outline color is the first one
        neighbors = grid.get_neighbors(x, y)
        color = grid.get_pixel(x, y)
        
        if ((neighbors[1][2]!=color and neighbors[1][2]!=outline_color) or
           (neighbors[2][1]!=color and neighbors[2][1]!=outline_color)):
            color = outline_color
            
        return color