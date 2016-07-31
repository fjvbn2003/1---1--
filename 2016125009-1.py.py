source = open("input.txt") #source라는 변수를 이용해서 input.txt를 open
read = source.readlines()
startread = [int(i) for i in read[0].split()] #startread라는 변수는 read의 첫번째 줄
                                              #즉 행렬의 크기를 나타내는 줄  
A = []
B = []
C = [[0 for i in range(startread[3])]for j in range(startread[0])] #C라는 리스트 생성


for i in range(1,startread[0]+1): #append함수를 이용하여 A라는 리스트를 생성
        A.append([int(j) for j in read[i].split()])

for i in range(startread[0]+1,startread[0]+startread[2]+1): #A와 마찬가지로 B생성
        B.append([int(j) for j in read[i].split()])



try:                        #try except문을 이용해 error 방지
    for m in range(startread[0]):
        for n in range(startread[3]):
            for k in range(startread[1]):
                C[m][n] = C[m][n]+A[m][k]*B[k][n]
except:
    print("cannot multiply") #index error 발생시
            
source.close()

with open("output.txt","w") as mat: #output.txt 를 작성
    for i in range(len(C)):
        for j in range(len(C[0])):
            C[i][j] = str(C[i][j])
    for i in C:
        mat.write(' '.join(i)+'\n')
    
