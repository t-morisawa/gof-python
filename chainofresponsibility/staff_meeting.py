from level import Level
from responsible import Responsible

class StaffMeeting(Responsible):
    def __init__(self, responsible_person):
        super(StaffMeeting, self).__init__(responsible_person)
        self.responsibleLevel = Level(4)

    def beAbleToJudge(self, question):
        return question.level.lessThan(self.responsibleLevel)

    def judge(self, question):
        print('{}がjudgeします'.format(self.responsible_person))
