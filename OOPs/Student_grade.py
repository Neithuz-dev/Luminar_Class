from typing import Self


class Student:
    school_name = "St.Joseph's School"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >90:
            return "A grade"
        elif self.marks>=75:
            return "B grade"
        else:
            return "C grade"

    def display(self):
        print("Student Name:",self.name)
        print("School Name:",Student.school_name)
        print("Mark:",self.marks)
        print("Grade:",self.grade())

stu = Student("Mariya",85)
stu.display()