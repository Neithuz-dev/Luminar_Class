# st = {"hi",9,5,6, "python",8,7}
# print(st)
#
# st1 = {}
# print(type(st1))
#
# st2 = set()
# print(type(st2))

st = {9,8,7,6,8,9,8,4,5}
#
# print(min(st))
# print(len(st))
#
#
# st.add(12)
# print(st)
#
# st.update(([100,200,34]))
# print(st)
#
# st.remove(100)
# print(st)
ls =  [20,45,3,2]
for i in ls:
    if i in st:
        st.remove(1)
print(st)