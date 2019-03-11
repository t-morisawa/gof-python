from abc import ABCMeta, abstractmethod


class Teacher(metaclass=ABCMeta):
    def __init__(self):
        students = []

    @abstractmethod
    def visit(self, student_home):
        pass

    def getStudentList(self):
        return self.students
