# WHATIS: 計数ソート。ソートしたい整数の値が小さい時　安定
def CountingSort(A, B, k):
    C = [0] * (k+1)
    for i in range(k):
        C[i] = 0
    #C[i] に i の出現数を記録する 
    for j in range(0,n):
        C[A[j]]+=1
    #print("C ",j,C[:100])
    #C[i] に i 以下の数の出現数を記録する
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]
    #print("C' ",j,C[:100])
    for j in range(n-1,-1,-1):
        B[C[A[j]]] = A[j]
        C[A[j]]-=1
        #print(j,A[j],C[A[j]],B[C[A[j]]],B,C)

n = int(input())
A = list(map(int,input().split()))
B = [0] * (n+1)
CountingSort(A,B,100000)
print(' '.join(map(str,B[1:])))