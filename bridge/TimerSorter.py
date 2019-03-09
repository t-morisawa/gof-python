from datetime import datetime
from Sorter import Sorter


class TimerSorter(Sorter):
    def timerSort(self, list_):
        start = datetime.now()
        self.sort(obj)
        end = datetime.now()
        print("time:"+(end - start))
