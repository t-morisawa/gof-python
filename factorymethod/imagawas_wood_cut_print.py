from wood_cut_print import WoodCutPrint
from potato import Potato

class ImagawasWoodCutPrint(WoodCutPrint):
    def draw(self, hanzai):
        print('マンガの絵を描く')

    def cut(self, hanzai):
        print('彫刻刀を利用して器用に彫る')

    def print_(self, hanzai):
        print('インクとして、自分の血を使いプリントする')

    def createCuttable(self):
        return Potato()
