class a :
    k = []
    def __init__(self): # 초기화
        self.result = 0

    def push (self, num):
        self.k.append(int(num))

    def front (self):
        try :print(self.k[0])

        except:
            print('-1')
    def back (self):
        try :print(self.k[-1])

        except:
            print('-1')
    def size (self):
        print(len(self.k))

    def empty (self):

        if len(self.k) == 0 :
            print('1')
        else :
            print ('0')
    def pop (self):

        try:
            print(self.k[0])
            del self.k[0]
           

        except:
            print('-1')
    
b = a()
m  = int(input())

for i in range(m):
    l = input()
    if 'push' in l:
        x = l.split() # x는 push 에서 입력받은 글자를 불리시켜만든 리스트
        b.push(x[1])
    else:
        exec('b.'+l+'()')
        
