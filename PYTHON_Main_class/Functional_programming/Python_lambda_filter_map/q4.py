# Question 4: Convert Passed Students' Marks into Grades
# Question
# Select students who scored 50 or above. Then assign grades:
# 90 and above → A
# 75–89 → B
# 50–74 → C
marks = [45, 82, 91, 68, 37, 78]
# Output: ['B', 'A', 'C', 'B']
ls = list(map(lambda x: "A" if x>=90 else "B"
                if x>=75 else "C"
              ,filter(lambda x:x>50,marks)))
print(ls)