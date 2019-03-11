from abc import ABCMeta, abstractmethod
from student import Student
from class_teacher import ClassTeacher
from chief_teacher import ChiefTeacher
from staff_meeting import StaffMeeting
from question import Question
from level import Level

if __name__ == '__main__':
    nakagawa = Student("中川雄介")
    rookie = ClassTeacher("新人先生")
    veteran = ChiefTeacher("ベテラン先生")
    staffMeeting = StaffMeeting("職員会議")
    nakagawa.setNext(rookie).setNext(veteran).setNext(staffMeeting)
    nakagawa.judge(Question("おやつはいくらまで？",Level(1)))
    nakagawa.judge(Question("携帯電話持って行ってよい？",Level(3)))
