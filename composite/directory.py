from file_ import File

class Directory:
    def  __init__(self, name):
        self.name = name
        self.list_ = []

    def append(self, obj_):
        self.list_.append(obj_)

    def remove(self):
        for item in self.list_:
            if(isinstance(item, File)):
                item.remove()
            elif(isinstance(item, Directory)):
                item.remove()
            else:
                System.out.println("削除できません")
        print(self.name + "を削除しました。")
