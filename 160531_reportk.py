##def reportk1 (a,b,k):
##    for i in a:
##        for j in b:
##            if (i + j ==k):
##                print(i,j)

##def reportk2(a,b,k):
##    for i in a:
##        j = k - i
##        if j in b:
##            print(i,j)
##
import random

def reportk3 (A,B,k):
    index = len(B) -1

    for a in A:
        while (index >=0) and (a+B[index] > k):
            index = index -1

        if index <0:
            continue
        if a+B[index] == k:
            print(a,B[index])
                    


m = random.sample(range(1000),10)
n = random.sample(range(1000),10)


