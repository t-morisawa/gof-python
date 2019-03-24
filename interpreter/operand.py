from abc import ABCMeta, abstractmethod


class Operand(metaclass=ABCMeta):
    @abstractmethod
    def get_operand_string(self):
        pass


class Ingredient(Operand):
    """
    処理対象を表すクラス
    """
    def __init__(self, operand_string):
        self.operand_string = operand_string

    def get_operand_string(self):
        return self.operand_string


class Expression(Operand):
    """
    処理結果を表すクラス
    """
    def __init__(self, operator):
        self.operator = operator

    def get_operand_string(self):
        return self.operator.execute().get_operand_string()
