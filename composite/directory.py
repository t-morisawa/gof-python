from file_ import File
from directory_entry import DirectoryEntry


class Directory(DirectoryEntry):
    def  __init__(self, name):
        self.name = name
        self.list_ = []

    def append(self, obj_):
        self.list_.append(obj_)

    def remove(self):
        for item in self.list_:
            item.remove()
        print(self.name + "を削除しました。")
