from file_ import File
from directory import Directory

if __name__ == '__main__':
    file1 = File("file1")
    file2 = File("file2")
    file3 = File("file3")
    file4 = File("file4")
    dir1 = Directory("dir1")
    dir1.append(file1)
    dir2 = Directory("dir2")
    dir2.append(file2)
    dir2.append(file3)
    dir1.append(dir2)
    dir1.append(file4)
    dir1.remove()
