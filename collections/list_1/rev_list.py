# A software tool needs to reverse every keyword before storing it in memory.
#
# Example Input:
# keywords = ["python", "java", "html"]
#
# Output:
# ['nohtyp', 'avaj', 'lmth']

keywords = ["python", "java", "html"]
def Rev():
    new_ls = []
    for word in keywords:
        new_ls.append(word[::-1])
    print(new_ls)

Rev()