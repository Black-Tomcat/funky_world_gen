class Terrain:
    def __init__(self, name, color, height_range=False, height=False):
        self.name = name
        self.color = color

        if height == False:
            self.height_range = height_range
        elif list(height_range)[0] <= height < list(height_range)[-1] + 1:
            self.height = height
        else:
            raise Exception("Height range or height not specified correctly")

    def create_copy(self, height):
        return Terrain(self.name, self.color, self.height_range, height)
