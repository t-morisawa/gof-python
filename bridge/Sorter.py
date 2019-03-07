from abc import ABCMeta, abstractmethod

class Sorter(ABCMeta):
    @abstractmethod
    def sort(list_):
        pass
