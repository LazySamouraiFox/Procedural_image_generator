#### Color palette manager ####

class Palette:
    
    def __init__(self):
        self.colors = [
            (28, 28, 28),      # 0 - Dark
            (80, 80, 80),      # 1 - Gray
            (160, 160, 160),   # 2 - Light Gray
            (240, 240, 240),   # 3 - White
            (0, 140, 255),     # 4 - Blue
            (0, 200, 120),     # 5 - Green
            (255, 170, 0),     # 6 - Orange
            (220, 60, 60)]     # 7 - Red

    def size(self):
        return len(self.colors)

    def get_color(self, index):
        return self.colors[index]