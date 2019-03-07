import ingregients
from hotpot import HotPot

if __name__ == '__main__':
    hotpot = HotPot(ingregients.Pot())
    hotpot.addSoup(ingregients.ChickenBonesSoup())
    hotpot.addMain(ingregients.Chicken())
    hotpot.addVegetables([
        ingregients.ChineseCabbage(),
        ingregients.Leek(),
        ingregients.Chrysanthemum()
    ])
    hotpot.otherIngredients([
        ingregients.Tofu()
    ])
