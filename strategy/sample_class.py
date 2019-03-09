class SampleClass:
    def __init__(self, compare_type):
        self.COMPARE_AGE = 1
        self.COMPARE_HEIGHT = 2
        self.COMPARE_WEIGHT = 3
        self.type_ = type_

    def compare(h1, h2):
        if(type_ == self.COMPARE_AGE):
            if(h1.age > h2.age):
                return 1
            elif(h1.age == h2.age):
                return 0
            else:
                return -1
        elif(type_ == self.COMPARE_HEIGHT):
            if(h1.height > h2.height):
                return 1
            elif(h1.height == h2.height ):
                return 0
            else:
                return -1
        else:
            if(h1.weight > h2.weight):
                return 1
            elif(h1.weight == h2.weight ):
                return 0
            else:
                return -1
