from icecream import Icecream

class SliceAlmondToppingIcecream(Icecream):
    def __init__(self, ice):
        self.ice = ice

    def getName(self):
        name = "スライスアーモンド"
        name += self.ice.getName()
        return name

    def howSweet(self):
        return ice.howSweet()
