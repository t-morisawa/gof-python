from level import Level
from responsible import Responsible

class Student(Responsible):
    def __init__(self, responsible_person):
        super(Student, self).__init__(responsible_person)
        self.responsibleLevel = Level(1)

    def beAbleToJudge(self, question):
        return question.level.lessThan(self.responsibleLevel)

    def judge(self, question):
        print('{}がjudgeします'.format(self.responsible_person))
