from level import Level
from responsible import Responsible

class ChiefTeacher(Responsible):
    def __init__(self, responsible_person):
        super(ChiefTeacher, self).__init__(responsible_person)
        self.responsibleLevel = Level(3)

    def beAbleToJudge(self, question):
        return question.level.lessThan(self.responsibleLevel)

    def judge(self, question):
        print('{}がjudgeします'.format(self.responsible_person))
