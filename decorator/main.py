from vanilla_icecream import VanillaIcecream
from green_icecream import GreenTeaIcecream
from cashew_nuts_topping_icecream import CashewNutsToppingIcecream
from slice_almond_topping_icecream import SliceAlmondToppingIcecream


if __name__ == '__main__':
    ice1 = CashewNutsToppingIcecream(VanillaIcecream());
    ice2 = CashewNutsToppingIcecream(GreenTeaIcecream());
    ice3 = SliceAlmondToppingIcecream(CashewNutsToppingIcecream(VanillaIcecream()));
    print(ice1.getName())
    print(ice2.getName())
    print(ice3.getName())
