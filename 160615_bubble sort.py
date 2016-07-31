a = [3,1,0,2,9,45,4,6]
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
        else:
            continue
    print(a)
print(a)
