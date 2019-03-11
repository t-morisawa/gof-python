from abc import ABCMeta, abstractmethod


class DirectoryEntry(metaclass=ABCMeta):
    @abstractmethod
    def remove(self):
        pass
