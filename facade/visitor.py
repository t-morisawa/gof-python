# 山田くん
from librarian import Librarian


class Visitor:
    pass

if __name__ == '__main__':
    # 窓口の中村くんを作る
    nakamura = Librarian()
    # 中村くんに昆虫図鑑の場所を聞く
    location = nakamura.searchBook("昆虫図鑑")
    if location == "貸出中です":
        print("貸出中かよ…")
    elif location == "その本は所蔵していません":
        print("なんだ、ないのか")
    else:
        print("サンキュ！")
