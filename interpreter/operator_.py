from abc import ABCMeta, abstractmethod
from operand import Ingredient


class Operator(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class Plus(Operator):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def execute(self):
        return Ingredient(self.operand1.get_operand_string() + 'と' + self.operand2.get_operand_string() + 'を足したもの')


class Wait(Operator):
    def __init__(self, minutes, operand):
        self.minutes = minutes
        self.operand = operand

    def execute(self):
        return Ingredient(self.operand.get_operand_string() + 'を' + self.minutes.get_operand_string() + '分置いたもの')
