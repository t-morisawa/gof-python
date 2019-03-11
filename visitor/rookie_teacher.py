from teacher import Teacher
from home import Home
from tanaka_home import TanakaHome
from suzuki_home import SuzukiHome


class RookieTeacher(Teacher):
    def __init__(self, students):
        self.students = students

    def visit(self, student_home):
        if(isinstance(student_home, Home)):
            print("こんにちは")
        if(isinstance(student_home, TanakaHome)):
            student_home.praisedChild()
        if(isinstance(student_home, SuzukiHome)):
            student_home.reprovedChild()
