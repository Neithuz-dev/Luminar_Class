# # def prime(lower,upper):
# #     for num in range(lower,upper):
# #         if num>1:
# #             for i in range(2,num):
# #                 if num%i ==0:
# #                     print("not prime",num)
# #                     break
# #             else:
# #                 print("Prime", num)
# # prime(2,10)
# #
#
def prime(lower,upper):
    result = ""
    for num in range(lower,upper):
        if num <2:
            result+=  f"Not prime{num}\n"
        for i in range(2,upper):
            if num%i == 0:
                result+= f"Not prime{num}\n"
        else:
            result+= f"Prime{num}\n"
    return result


rs = prime(3,10)
print(rs)
