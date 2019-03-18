# 図書委員の中村くん
from lendinglist import LendingList
from booklist import BookList


class Librarian:
    def searchBook(self, bookName):
        # 本を探す
        book_list = BookList()
        location = book_list.searchBook(bookName)
        # 本の場所がnullではない(所蔵してる)とき
        if location is not None:
            # 貸出中かチェックする
            lending_list = LendingList()
            if lending_list.check(bookName):
                # 貸出中のとき
                return "貸出中です"
            else:
                # 貸出中ではないとき
                return location
        # 所蔵してないとき
        else:
            return "その本は所蔵していません"
