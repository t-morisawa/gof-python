import sys
from mizutaki_factory import MizutakiFactory
from hotpot import HotPot
from ingregients import Pot

def createFactory(string):
    if string == "キムチ鍋":
        return MizutakiFactory() # FIXME KimuchiFactory()
    else:
        return MizutakiFactory()

if __name__ == '__main__':
    hotpot = HotPot(Pot())
    if len(sys.argv) > 1:
        factory = createFactory(sys.argv[1])
    else:
        factory = MizutakiFactory()
    hotpot.addSoup(factory.getSoup())
    hotpot.addMain(factory.getMain())
    hotpot.addVegetables(factory.getVegetables())
    hotpot.addOtherIngredients(factory.getOtherIngredients())
