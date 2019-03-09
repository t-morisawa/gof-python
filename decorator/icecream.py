from abc import ABCMeta, abstractmethod

class IceCream(metaclass=ABCMeta):
    @abstractmethod
    def getName():
        pass

    @abstractmethod
    def howSweet():
        pass
