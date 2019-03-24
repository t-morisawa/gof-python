from operand import Ingredient, Expression
from operator_ import Plus, Wait


if __name__ == '__main__':
    """
    Expressionクラスを使わずにかく
    """
    salt = Ingredient('粉末スープ')
    noodle = Ingredient('麺')
    water = Ingredient('お湯')
    three = Ingredient('3')
    soup = Ingredient('液体スープ')

    ramen1 = Plus(salt, noodle).execute()
    ramen2 = Plus(ramen1, water).execute()
    ramen3 = Wait(three, ramen2).execute()
    ramen4 = Plus(ramen3, soup).execute()

    print(ramen4.get_operand_string())
