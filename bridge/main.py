from TimerSorter import TimerSorter
from BubbleSorter import BubbleSorter
from QuickSorter import QuickSorter

if __name__ == '__main__':
    bubble = BubbleSorter()
    quick = QuickSorter()
    list_ = [1,2,3]
    timerSorter = TimerSorter(bubble)
    timerSorter.sort(list_)
    timerSorter = TimerSorter(quick)
    timerSorter.sort(list_)
