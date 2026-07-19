num = input("entr the number: ")
for i in range(len(num)):
    rotations = int(num[i:] + num[:i])
    print(rotations)

    if rotations <2:
        print("Not cirular prime")
        break

    for n in range(2,rotations):
        if rotations %n ==0:
            print("Not cirular")
            break
    else:
        print("cirular")
