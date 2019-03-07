from teacher import Teacher

if __name__== '__main__':
   teacher = Teacher()
   papers = teacher.createManyCrystals()
   print(papers)
   papers = teacher.createManyCrystalsAndTrees()
   print(papers)
