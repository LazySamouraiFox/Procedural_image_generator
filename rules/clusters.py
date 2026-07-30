#### Clustering rules ####

class ClusterRules:
    
    def __init__(self, range=1):
        self.range = range
    
    def plus_clusters(self, x, y, grid):
        
        r = self.range
        neighbors = grid.get_neighbors(x, y, r)
        color = grid.get_pixel(x, y)
        
        left   = neighbors[r][0]     
        bottom = neighbors[2*r][r]    
        right  = neighbors[r][2*r]
        top    = neighbors[0][r]   
        

        if (left is not None and
            left == bottom and
            right == top and
            right == bottom):
            color = left   
                        
        return color

    def multiply_clusters(self, x, y, grid):
        
        r = self.range
        neighbors = grid.get_neighbors(x, y, r)
        color = grid.get_pixel(x, y)

        bottom_left  = neighbors[2*r][0]   
        bottom_right = neighbors[2*r][2*r] 
        top_right    = neighbors[0][2*r]   
        top_left     = neighbors[0][0]    
        
        if (bottom_left is not None and
            bottom_left == bottom_right and
            top_right == top_left and
            top_right == bottom_right):
            color = bottom_left   
                        
        return color
    