from abc import ABCMeta, abstractmethod
from wood import Wood

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

    def createCuttable(self):
        return Wood()

    def createWoodCutPrint(self):
        hanzai = self.createCuttable()
        print(type(hanzai))
        self.draw(hanzai)
        self.cut(hanzai)
        self.print_(hanzai)
