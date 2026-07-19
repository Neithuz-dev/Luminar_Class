# PR 7
#
# Count Passed and Failed Students
#
# Context:
# Enter marks for N students.
# Pass mark = 40.
n = int(input("enter the no of students: "))
count_pass=0
count_fail =0
for i in range (n):
    mark = int(input("enter the mark: "))
    if mark >=40:
        count_pass+=1
    else:
        count_fail+=1
print("No of pass:",count_pass)
print("No of fail:",count_fail)