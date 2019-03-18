from abc import ABCMeta, abstractmethod


class LoveMeditator(metaclass=ABCMeta):
    @abstractmethod
    def addColleague(self, colleague):
        pass

    @abstractmethod
    def consultation(self, colleague, lover):
        pass


class Saito(LoveMeditator):
    def __init__(self):
        self.map_ = {}

    def addColleague(self, colleague):
        self.map_[colleague.get_name()] = colleague

    def consultation(self, colleague, lover):
        possibility = 0
        # さまざまな状況を考慮して、possibility を導出
        return possibility
