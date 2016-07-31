a = int(input())

b = [int(i) for i in input().split()]






isprime = [True]*1001

isprime[0] = False
isprime[1] = False

for i in range(2,1001):
    if isprime[i]:
        j = i*2
        while(j<=1000):
            isprime[j] = False
            j = j+i
cnt = 0
for i in b:
    if isprime[i]:
        cnt += 1
    else:
        continue

print (cnt)
