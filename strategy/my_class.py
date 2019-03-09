from age_comparator import AgeComparator

class MyClass:
    def __init__(self, comparator):
        self.comparator = comparator
    def compare(self, h1, h2):
        return self.comparator.compare(h1, h2)
