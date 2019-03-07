from factory import Factory
from ingregients import ChickenBonesSoup, Chicken, ChineseCabbage, Leek, Chrysanthemum, Tofu

class MizutakiFactory(Factory):
    def getSoup(self):
        return ChickenBonesSoup()

    def getMain(self):
        return Chicken()

    def getVegetables(self):
        vegetables = []
        vegetables.append(ChineseCabbage())
        vegetables.append(Leek())
        vegetables.append(Chrysanthemum())
        return vegetables

    def getOtherIngredients(self):
        otherIngredients = []
        otherIngredients.append(Tofu())
        return otherIngredients
