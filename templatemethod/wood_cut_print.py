from abc import ABCMeta, abstractmethod

class WoodCutPrint(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, hanzai):
        pass

    @abstractmethod
    def cut(self, hanzai):
        pass

    @abstractmethod
    def print_(self, hanzai):
        pass

    def createWoodCutPrint(self):
        hanzai = 'new Wood()'
        self.draw(hanzai)
        self.cut(hanzai)
        self.print_(hanzai)
