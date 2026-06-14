# 7.Count Passed and Failed Students
#
# You are a teacher in a class.
#
# You want to find how many students passed and how many failed.
#
# Rules:
#
# You will first enter the total number of students.
#
# Then you will enter marks for each student one by one.
#
# If a student’s mark is 40 or more, the student is Pass.
#
# If the mark is less than 40, the student is Fail.
#
# At the end, display:
#
# Total number of passed students
#
# Total number of failed students
students = int(input("Enter total number of students: "))
pass_count = 0
fail_count = 0
for i in range(students):
    marks = int(input("Enter marks: "))
    if marks >= 40:
        pass_count += 1
    else:
      fail_count += 1
print("Passed Students:", pass_count)
print("Failed Students:", fail_count)
