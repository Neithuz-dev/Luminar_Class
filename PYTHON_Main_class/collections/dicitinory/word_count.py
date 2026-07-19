# text = "techno lab hub kochin"
# word = text.split((" "))
# print(word)

text = "sky buy high high buy sky sky sky buy high sky sky"
# new_txt = text.split()
# count = {}
# for i in new_txt:
#     if i not in count:
#         count[i]=1
#     else:
#         count[i]+=1
#
# print(count)
new_tetx = text.split()
count = {}
def text_count(new_tetx):
    for i in new_tetx:
        if i not in count:
            count[i] = 1
        else:
            count[i]+=1
    print(count )

text_count(new_tetx)