from paper import Paper

class Teacher:
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
