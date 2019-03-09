from abc import ABCMeta, abstractmethod

class DirectoryEntry(metaclass=ABCMeta):
    @abstractmethod
    def remove():
        pass
