#### Pipeline manager that apply the rules along the generations ####

class Pass:
    def apply(self, grid):
        raise NotImplementedError

class RulePass(Pass):

    def __init__(self, rule, iterations=1):
        self.iterations = iterations
        self.rule = rule

    def apply(self, grid):
        
        old = grid
        new = grid.clone()
        width = old.width
        height = old.height
        
        for _ in range(self.iterations):
            for y in range(height):
                for x in range(width):
                    new_color = self.rule(x, y, old)                        
                    new.set_pixel(x, y, new_color)
            old, new = new, old
        
        return old