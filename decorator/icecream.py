from abc import ABCMeta, abstractmethod

class Icecream(metaclass=ABCMeta):
    @abstractmethod
    def getName():
        pass

    @abstractmethod
    def howSweet():
        pass
