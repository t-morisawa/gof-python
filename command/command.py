from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def set_beaker(self, beaker):
        self.beaker = beaker

    @abstractmethod
    def execute(self):
        pass


class AddSaltCommand(Command):
    def execute(self):
        print('食塩を1gずつ加える実験')
        while self.beaker.is_melted():
            self.beaker.add_salt(1)
            self.beaker.mix()
        self.beaker.note()


class AddWaterCommand(Command):
    def execute(self):
        print('水を10gずつ加える実験')
        while not self.beaker.is_melted():
            self.beaker.add_water(10)
            self.beaker.mix()
        self.beaker.note()


class MakeSaltWaterCommand(Command):
    def execute(self):
        print('食塩水を作る実験')
        self.beaker.mix()
        self.beaker.note()
