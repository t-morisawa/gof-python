from abc import ABCMeta, abstractmethod

# 由実ちゃんの状態を表すクラスが実装すべきインタフェース

class State(metaclass=ABCMeta):
    # 朝のあいさつを返すメソッドを定義する
    def morningGreet(self):
        pass

    # 寒いときの対策を返すメソッドを定義する
    def getProtectionForCold(self):
        pass


class BadMoodState(State):
    # 朝のあいさつです。機嫌の悪いときは、ぶっきらぼうに応えます。
    def morningGreet(self):
        return "おお"

    # 冬の防寒方法です。機嫌の悪いときはももひきをはきます。
    def getProtectionForCold(self):
        return "ももひき"


class OrdinaryState(State):
    # 朝のあいさつです。通常は、男らしく応えます。
    def morningGreet(self):
        return "おっす！"

    # 冬の防寒方法です。走るようです。
    def getProtectionForCold(self):
        return "走る"
