# def prime(num):
#     if num >1:
#         for i in range(2,num):
#             if num % i ==0:
#                 print("Not prime")
#                 break
#         else:
#             print("Prime")
#
#
# prime(7)
def prime(num):
    if num <2:
        return "Not prime"
    for i in range(2,num):
        if num%i == 0 :
            return "Not prime"
    else:
        return "prime"
print(prime(9))
