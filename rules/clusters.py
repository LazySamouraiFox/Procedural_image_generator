#### Clustering rules ####

def plus_sign_clusters(x, y, grid):
    
    neighbors = grid.get_neighbors(x, y)
    color=grid.get_pixel(x, y)
    
    if (neighbors[0]==neighbors[2] and
    neighbors[4]==neighbors[6] and
    neighbors[4]==neighbors[2]):
        print("Ouai !")
        color = neighbors[0]   
                    
    return color

def multiply_sign_clusters(x, y, grid):
    
    neighbors = grid.get_neighbors(x, y)
    color=grid.get_pixel(x, y)
    
    if (neighbors[1]==neighbors[3] and
    neighbors[5]==neighbors[7] and
    neighbors[5]==neighbors[3]):
        color = neighbors[1]   
                    
    return color
    