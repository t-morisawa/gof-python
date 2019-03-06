from cloneable import Cloneable

class Paper(Cloneable):
    def __init__(self, text=''):
        self.name = text

    def createClone(self):
        newPaper = Paper()
        newPaper.name = self.name
        return newPaper
