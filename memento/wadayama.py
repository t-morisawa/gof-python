from calc import Calc


# 計算する和田山君クラス。
class Wadayama:
    def __init__(self):
        self.map_ = {}


if __name__ == "__main__":
    wdym = Wadayama()
    calc = Calc()
    for i in range(1, 6):
        calc.plus(i)

    print(calc.getTemp())
    wdym.map_["5までの足し算"] = calc.createMemento()

    # 数日経過
    # 10までの足し算をしたい。

    calc2 = Calc()
    calc2.setMemento(wdym.map_.get("5までの足し算"))
    for i in range(6, 11):
        calc2.plus(i)
    print(calc2.getTemp())
    wdym.map_["10までの足し算"] = calc2.createMemento()