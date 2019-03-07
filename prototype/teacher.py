from paper import Paper
from prototype_keeper import PrototypeKeeper

class Teacher:
    def createManyCrystalsAndTrees(self):
        paper1 = Paper('雪の結晶')
        paper2 = Paper('もみの木')
        keeper = PrototypeKeeper()
        keeper.addCloneable('snowflake', paper1)
        keeper.addCloneable('tree', paper2)
        papers = []
        for i in range(100):
            papers.append(keeper.getClone('snowflake'))
            papers.append(keeper.getClone('tree'))
        return papers;

    def createManyCrystals(self):
        paper = Paper('雪の結晶')
        self.drawCrystal(paper);
        self.cutAccordanceWithLine(paper);
        papers = []
        for i in range(100):
            papers.append(paper.createClone())
        return papers;

    def drawCrystal(self, paper):
        # きれいに描くため時間がかかる
        pass

    def cutAccordanceWithLine(self, paper):
        # 描かれた線に沿ってきれいに切るには時間がかかる
        pass
