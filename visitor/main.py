from suzuki_home import SuzukiHome
from tanaka_home import TanakaHome
from rookie_teacher import RookieTeacher


if __name__ == '__main__':
    suzuki = SuzukiHome()
    tanaka = TanakaHome()
    rookie = RookieTeacher([suzuki, tanaka])
    for home in rookie.getStudentList():
        home.accept(rookie)
