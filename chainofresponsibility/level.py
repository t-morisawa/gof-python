class Level:
    def __init__(self, level):
        self.level = level

    def lessThan(self, level):
        return self.level < level.level