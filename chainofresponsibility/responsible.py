from abc import ABCMeta, abstractmethod


class Responsible(metaclass=ABCMeta):
    def __init__(self, responsible_person):
        self.responsible_person = responsible_person

    def setNext(self, next_):
        self.next_ = next_
        return next_

    def putQuestion(self, question):
        if(self.beAbleToJudge(question)):
            self.judge(question)
        elif(next != None):
            self.next_.putQuestion(question)
        else:
            print("誰にも判断できませんでした。やってみなさい。")

    @abstractmethod
    def beAbleToJudge(self, question):
        pass

    @abstractmethod
    def judge(self, question):
        pass
