import re

def BubbleSort(C, N, A):
    for i in range(0,N,1):
        for j in range(N-1, i, -1):
            #print(str(N)+' '+str(i)+' '+str(j))
            if C[j] < C[j-1]:
                C[j],C[j-1] = C[j-1],C[j]
                A[j],A[j-1] = A[j-1],A[j]
            #print(A)
    return A

def SelectionSort(C, N, A):
    for i in range(0,N,1):
        minj = i
        for j in range(i,N,1):
            #print(str(N)+' '+str(i)+' '+str(j))
            if C[j] < C[minj]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
        A[i], A[minj] = A[minj], A[i]
        #print(A)
    return A

if __name__ == '__main__':
    #print(list(range(0,5,1)))
    N = int(input())
    A = input()
    C = list(map(int,re.sub(r'\D', ' ', A).split()))
    CC = list(re.sub(r'[^A-Z]', ' ', A).split())
    A = A.split()

    BSA = BubbleSort(C[:],N,A[:])
    print(' '.join(BSA))
    print('Stable')
    SSA = SelectionSort(C[:],N,A[:])
    print(' '.join(SSA))
    print('Stable' if (BSA == SSA) else 'Not stable')
    





