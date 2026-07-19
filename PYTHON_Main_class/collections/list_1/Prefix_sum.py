# Description: Write a function that returns a new list where each element at index i is the sum of all elements from the original list up to index i.
# Input/Output Example
# •	Input: [1, 2, 3, 4]
# •	Output: [1, 3, 6, 10]
# o	(Calculation: [1, 1+2, 1+2+3, 1+2+3+4])
Input= [1, 2, 3, 4]
sum_ele =0
sum_list=[]
for i in Input:
    sum_ele +=i
    sum_list.append(sum_ele)
print(sum_list)
    