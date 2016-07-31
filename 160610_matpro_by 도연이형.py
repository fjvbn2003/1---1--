def matrix_product(A,B):
    res = []
    if(len(A[0])!=len(B)):
        return print("not product",len(A[0]),len(B))
    for a in range(len(A)):
        row = []
        
        for c in range(len(A[0])):
            value = 0
            for b in range(len(B[0])):
                value += A[a][b]*B[b][c]
            
            row.append(value)
        res.append(row)

    print(res)

a = [ [1,2] , [3,4] ]
b = [ [1,2] , [4,5] ]
c = matrix_product(a,b)
