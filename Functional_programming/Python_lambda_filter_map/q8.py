# Question 8: Find Students Eligible for a Scholarship
# Question
# Students scoring 80 or above are eligible for a scholarship. Increase their marks by 5 grace marks.
marks = [75, 82, 91, 68, 88, 79]
# Output: [87, 96, 93]
ls = list(map(lambda x:x+5,filter(lambda x:x>=80,marks)))
print(ls)
