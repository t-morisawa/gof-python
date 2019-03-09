from icecream import Icecream

class CashewNutsToppingIcecream(Icecream):
    def __init__(self, ice):
        self.ice = ice

    def getName(self):
        name = "カシューナッツ"
        name += self.ice.getName()
        return name

    def howSweet(self):
        return ice.howSweet()
