from human import Human
from my_class import MyClass
from age_comparator import AgeComparator

if __name__ == '__main__':
    h1 = Human('nao', 50, 20)
    h2 = Human('yk', 50, 21)
    c8r = AgeComparator()
    my_class = MyClass(c8r)
    print(my_class.compare(h1, h2))
