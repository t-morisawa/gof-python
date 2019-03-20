from abc import ABCMeta, abstractmethod

# 由実ちゃんの状態を表すクラスが実装すべきインタフェース

class State(metaclass=ABCMeta):
    # 朝のあいさつを返すメソッドを定義する
    def morningGreet(self):
        pass

    # 寒いときの対策を返すメソッドを定義する
    def getProtectionForCold(self):
        pass
