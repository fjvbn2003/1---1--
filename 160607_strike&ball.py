import random
a = random.sample(range(5),3)

print(a)
while True:
    k = [int(i) for i in input().split()]
    strike = 0
    ball = 0
    for i in k:
        if k.count(i)>1:
            print("duplicate number")
            break
        else:
            if (i in a) and (a.index(i) == k.index(i)):
                strike = strike+1
            if (i in a) and (a.index(i) != k.index(i)):
                ball = ball+1
            else:
                continue
    print(strike," strike", ball," ball")
            
