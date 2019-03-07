from abc import ABCMeta, abstractmethod

class Pot:
    pass

class Soup(metaclass=ABCMeta):
    pass

class Protein(metaclass=ABCMeta):
    pass

class Vegetable(metaclass=ABCMeta):
    pass

class Ingredients(metaclass=ABCMeta):
    pass

class ChickenBonesSoup(Soup):
    pass

class Chicken(Protein):
    pass

class ChineseCabbage(Vegetable):
    pass

class Leek(Vegetable):
    pass

class Chrysanthemum(Vegetable):
    pass

class Tofu(Ingredients):
    pass
