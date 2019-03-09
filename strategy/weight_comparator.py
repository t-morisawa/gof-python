class WeightComparator(Comparator):
    def compare(self, h1, h2):
        if(h1.weight > h2.weight):
            return 1
        elif(h1.weight == h2.weight):
            return 0
        else:
            return -1
