from mizutaki_factory import MizutakiFactory
from hotpot import HotPot
from ingregients import Pot

if __name__ == '__main__':
    hotpot = HotPot(Pot())
    factory = MizutakiFactory()
    hotpot.addSoup(factory.getSoup())
    hotpot.addMain(factory.getMain())
    hotpot.addVegetables(factory.getVegetables())
    hotpot.addOtherIngredients(factory.getOtherIngredients())
