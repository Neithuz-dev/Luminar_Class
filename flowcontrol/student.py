#chck if the student has atleast 75% attendance
attended = int(input("enter the number of classes attended "))
total_classes = int(input("enter the number of total classes "))
percentage = (attended*100)/total_classes
print("Attendance percentage is ",percentage)
if percentage>75:
    print("The student is Eligibile ")
else:
    print("The student is Not Eligibile ")