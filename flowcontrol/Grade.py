mark = int(input("Enter the mark of the student: "))
grade = " "
if mark <= 100 and mark >=0 :
  if mark > 90:
      grade="A"
  elif mark >80 and mark <= 90:
      grade = "B"
  elif mark > 70 and mark <=80:
      grade = "C"
  elif mark >60 and mark <= 70:
      grade ="D"
  else:
      grade = "Fail"
else:
    print("Invalid mark")
print("Your grade is ",grade)