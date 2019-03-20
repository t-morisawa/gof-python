class StatePatternYumichan():
    # 由実ちゃんの状態を表すプロパティ
    def __init__(self):
        self.state = None

    # 由実ちゃんの状態を変更するメソッド
    # @param state
    def changeState(self, state):
        self.state = state

    # 朝のあいさつを返すメソッド
    # @return
    def morningGreet(self):
        return self.state.morningGreet()

    # 寒いときの対策を取得するメソッド
    # @return
    def getProtectionForCold(self):
        return self.state.getProtectionForCold()
