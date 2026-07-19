class Students:
    def __init__(self,name,std,grade):
        self.name  = name
        self.std = std
        self.grade = grade

    def into(self):
        print("Student name:",self.name)
        print("Student Std:",self.std)

    def mark(self):
        print("Student grade:",self.grade)


ob1 = Students("neithal",10,"A+")
ob1.into()
ob1.mark()