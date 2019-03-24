from beaker import Beaker


if __name__ == "__main__":
    beaker = Beaker(100, 0)
    beaker.experiment(Beaker.ADD_SALT)

    beaker2 = Beaker(0, 10)
    beaker2.experiment(Beaker.ADD_WATER)
