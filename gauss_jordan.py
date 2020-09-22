import numpy as np

def pprint(msg, A):
    print("---", msg, "---")
    (n,m) = A.shape
    for i in range(0,n):
        line = ""
        for j in range(0,m):
            line += "{0:2f}".format(A[i,j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")


def gauss(A):
    (n,m) = A.shape()

    for i in range(0,n):
        maxEI = abs(A[i,i])
        maxRow = i
        for k in range(i+1,n):
            if abs(A[k,i]) > maxEI:
                maxEI = abs(A[k,i])
                maxRaw = k
    
        for k in range(i, m ):
            tmp = A[maxRow, k]
            A[maxRow,k] = A[i,k]
            A[i,k] = tmp
        
        piv = A[i,i]
        for k in range(i,m):
            A[i,k] = A[i,k]/piv
        
        for k in range(0,n):
            if k != i:
                c = A[k,i]/A[i,i]
                for j in range(i,m):
                    if i ==j:
                        A[k,j] = 0
                    else:
                        A[k,j] = A[k,j] - c * A[i,j]
        pprint(str(i+1)+"번째 반복",A) 

        x = np.zero
