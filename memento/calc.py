# ひとつの計算を表すクラス。
class Calc:
    def __init__(self):
        self.temp = 0

    # 足し算を実行するメソッド
    # @param plus
    def plus(self, plus):
        self.temp += plus

    # 途中経過を Memento として取得するメソッド
    # @return memento
    def createMemento(self):
        return self.Memento(self.temp)

    # Memento から計算経過を取得して、temp にセットする
    # @param memento
    def setMemento(self, memento):
        self.temp = memento.result

    # 計算結果を取得するメソッド
    # @return temp
    def getTemp(self):
        return self.temp

    # 途中経過を保持する Memento クラス
    class Memento():
        # 計算経過を引数に受け取るコンストラクタ
        # @param temp
        def __init__(self, temp):
            self.result = temp
