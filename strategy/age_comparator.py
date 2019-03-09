class AgeComparator:
    def compare(self, h1, h2):
        if(h1.age > h2.age):
            return 1
        elif(h1.age == h2.age):
            return 0
        else:
            return -1
