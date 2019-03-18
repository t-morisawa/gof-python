from abc import ABCMeta, abstractmethod
from love_meditator import Saito


class Colleague(metaclass=ABCMeta):
    @abstractmethod
    def needsAdvice(self):
        pass

    @abstractmethod
    def setSecretLover(self):
        pass


class Reina(Colleague):
    def __init__(self):
        self.name = "玲奈"
        self.tension = 0
        self.secretLover = None
        self.mediator = Saito()

    def getName(self):
        return self.name

    def setSecretLover(self, colleague):
        self.secretLover = colleague

    def needsAdvice(self):
        self.tension = self.mediator.consultation(self, self.secretLover)


class Nitta(Colleague):
    def __init__(self):
        self.name = "新田"
        self.tension = 0
        self.secretLover = None
        self.mediator = Saito()

    def getName(self):
        return self.name

    def setSecretLover(self, colleague):
        self.secretLover = colleague

    def needsAdvice(self):
        self.tension = self.mediator.consultation(self, self.secretLover)


if __name__ == '__main__':
    nitta = Nitta()
    reina = Reina()
    nitta.setSecretLover(reina)
    nitta.needsAdvice()
    print('{}のテンションは{}です'.format(nitta.getName(), nitta.tension))
