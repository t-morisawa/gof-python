from abc import ABCMeta, abstractmethod

class Cloneable(metaclass=ABCMeta):
    @abstractmethod
    def createClone():
        pass
