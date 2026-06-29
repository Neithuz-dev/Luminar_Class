def maxMaintainedRepo(resolved,required,k):
    need = []

    for i in range(len(resolved)): #3
        extra = required[i]-resolved[i] # 51-24 = 27 , 52-27 = 25
        if extra <=0:
            need.append(0)
        else:
            need.append(extra)
    need.sort()

    maintained = 0

    for x in need:
        if x <=k: #25<=100
            k-=x #100-25 # 100-27
            maintained+=1
        else:
            break
    return maintained


resolved  = [24,27,0]
required = [51,52,100]
k = 100

print(maxMaintainedRepo(resolved,required,k))