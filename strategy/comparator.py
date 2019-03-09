from abc import ABCMeta, abstractmethod

class Comparator(metaclass=ABCMeta):
    @abstractmethod
    def compare(h1, h2):
        pass
