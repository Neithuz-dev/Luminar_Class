# Problem 3: Employee Salary Analysis
# Question
# A company stores employee salaries.
# Find the average salary.
# Input
# {
#     "Rahul":50000,
#     "Asha":60000,
#     "Arun":55000
# }
# Output
# Average Salary = 55000
details = {
    "Rahul":50000,
    "Asha":60000,
    "Arun":55000
}
def avg_sal(details):
    # total = 0
    # count = 0
    # for name,sal in details.items():
    #     total += sal
    #     count+=1
    #
    # avg = total/count
    # print(avg)

#     avg_ = sum(details.values())/len(details)
#     print(avg_)
#
# avg_sal(details)
    avg_ = sum(details.values())/len(details)
    return avg_

print(avg_sal(details))