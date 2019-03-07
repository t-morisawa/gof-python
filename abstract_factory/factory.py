from abc import ABCMeta, abstractmethod

class Factory(metaclass=ABCMeta):
    @abstractmethod
    def getSoup(self):
        pass

    @abstractmethod
    def getMain(self):
        pass

    @abstractmethod
    def getVegetables(self):
        pass

    @abstractmethod
    def getOtherIngredients(self):
        pass
