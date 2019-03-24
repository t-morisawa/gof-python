from beaker import Beaker
from command import AddSaltCommand, AddWaterCommand, MakeSaltWaterCommand


if __name__ == "__main__":
    add_salt = AddSaltCommand()
    add_water = AddWaterCommand()
    make_salt_water = MakeSaltWaterCommand()

    add_salt.set_beaker(Beaker(100, 0))
    add_water.set_beaker(Beaker(0, 10))
    make_salt_water.set_beaker(Beaker(90, 10))

    add_salt.execute()
    add_water.execute()
    make_salt_water.execute()
