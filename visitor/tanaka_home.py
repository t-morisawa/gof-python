from home import Home
from teacher_acceptor import TeacherAcceptor


class TanakaHome(Home, TeacherAcceptor):
    def praisedChild(self):
        print("あら、先生ったらご冗談を")
        return Tea()

    def reprovedChild(self):
        print("うちの子に限ってそんなことは・・・。")
        return None

    def accept(self, teacher):
        teacher.visit(self)


class Tea():
    pass
