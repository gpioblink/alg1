cnt = 0
def insertionSort(A, n, g):
    for i in range(g,n,1):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt+=1
        A[j+g] = v

def shellSort(A, n):
    m = ?
    G[] = {?, ?,..., ?}
    for i in range(0,m,1):
        insertionSort(A, n, G[i])