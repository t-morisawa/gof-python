from abc import abstractmethod

# 先生インターフェース
class Teacher():
    @abstractmethod
    def question1(self):
        pass

    @abstractmethod
    def question2(self):
        pass

    @abstractmethod
    def question3(self):
        pass


class Yamada(Teacher):
    def question1(self):
        print("(解答1)")

    def question2(self):
        print("(解答2)")

    def question3(self):
        print("(解答3)")


class Fujiwara(Teacher):
    def __init__(self):
        self.yamada = Yamada()

    def question1(self):
        print("それは「～～解答1～～」です。")

    def question2(self):
        print("それは「～～解答2～～」です。")

    def question3(self):
        print("答えは「")
        self.yamada.question3()
        print("」となります。")
