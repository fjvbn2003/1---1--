a = open('12345.txt')
b= a.readline() #b = ['1 3 5 9 11']
print(b)
c = []
for i in b.split():
        c.append(int(i))
print(c)
