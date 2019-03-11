from teacher import Teacher
from home import Home


class RookieTeacher(Teacher):
    def __init__(self, students):
        self.students = students

    def visit(self, student_home):
        if(isinstance(student_home, Home)):
            print("こんにちは")
        if(isinstance(student_home, TanakaHome)):
            print("こんにちは")
        if(isinstance(student_home, SuzukiHome)):
            print("こんにちは")

    def visit(self, TanakaHome studentHome):
        studentHome.praisedChild();

    def visit(self, SuzukiHome studentHome){
        studentHome.reprovedChild();
    }
}

