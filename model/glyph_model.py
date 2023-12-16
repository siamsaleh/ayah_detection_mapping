class Glyph:

    def __init__(self, page, index, line, position, min_x, min_y, max_x, max_y):
        self.page = page
        self.index = index
        self.line = line
        self.position = position
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def print_values(self):
        print(f'page {self.page} index {self.index} line {self.line} pos {self.position} minx-{self.min_x} '
              f'miny-{self.min_y} maxx-{self.max_x} maxy-{self.max_y}')

