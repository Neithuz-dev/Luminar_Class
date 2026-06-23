# you are given a list of words ls and a target word.
# your task is to find how many times the target word appears in the list.
#
# example:
# ls= ['sun','moon','sun','sky','sun','sun','moon','sun','sky']
# word = 'sun'
#
# output:
# 5
ls= ['sun','moon','sun','sky','sun','sun','moon','sun','sky']
word = 'sun'
def Count():
    count_sun = 0
    for i in ls:
        if i == word:
            count_sun+=1
    print(count_sun)

Count()
