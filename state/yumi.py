class Yumichan():
    STATE_ORDINARY = 0
    STATE_IN_BAD_MOOD = 1

    # 由実ちゃんの状態を表すプロパティ
    def __init__(self):
        self.state = -1

    # 由実ちゃんの状態を変更するメソッド
    # @param state
    def changeState(self, state):
        if state == STATE_ORDINARY:
            return "おっす!"
        elif state == STATE_IN_BAD_MOOD:
            return "おお"
        else:
            return "・・・"

    # 朝のあいさつを返すメソッド
    # @return
    def morningGreet(self):
        if state == STATE_ORDINARY:
            return "走る"
        elif state == STATE_IN_BAD_MOOD:
            return "ももひきをはく"
        else:
            return "・・・"

    # 寒いときの対策を取得するメソッド
    # @return
    def getProtectionForCold(self):
        return self.state.getProtectionForCold()
