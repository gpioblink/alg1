# WHATIS: 挿入ソート

def nsertionSort(A, N): #N個の要素を含む0-オリジンの配列A
    print(" ".join(map(str,A)))
    for i in range(1,N,1):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j-=1
            A[j+1] = v
        print(" ".join(map(str,A)))

if __name__ == "__main__":
    N = int(input())
    A = list(map(int,input().split()))
    nsertionSort(A,N)