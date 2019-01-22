def partition(A, p, r):
  x = A[r]
  i = p-1
  for j in range(p,r):
    if A[j] <= x:
      i = i+1
      A[i], A[j] = A[j], A[i]
  A[i+1],A[r] = A[r], A[i+1]
  return i+1

n = int(input())
A = list(map(int, input().split()))
mid = partition(A,0,n-1)
print(' '.join(map(str,A[:mid])),'['+str(A[mid])+']',' '.join(map(str,A[mid+1:])))