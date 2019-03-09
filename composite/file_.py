from directory_entry import DirectoryEntry

class File(DirectoryEntry):
    def __init__(self, name):
        self.name = name

    def remove(self):
        print(self.name + "を削除しました");
