b = input('Enter file name')
f = open(b,'w')

while True:
    
    c = input()
    if c =='.':
        break
    f.write(c+'\n')

f.close()
