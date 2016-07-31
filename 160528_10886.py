

while True:
    a = int(input())
    b = ''
    for i in range(a):
        b +=(input())

    if b.count('1')>b.count('0'):
        print('Junhee is cute!')
    else:
        print("Junhee is not cute!")
