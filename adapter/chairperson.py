from abc import ABCMeta, abstractmethod

class Chairperson(metaclass=ABCMeta):
    @abstractmethod
    def organizeClass(self):
        pass
