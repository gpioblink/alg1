cnt = 0
def merge(A, left, mid, right):
  global cnt
  #print("marge ",A,left,mid,right)
  n1 = mid - left
  n2 = right - mid
  #L = [0] * (n1+1)
  #R = [0] * (n2+1)
  L = [0] * (n1+1)
  R = [0] * (n2+1)
  
  for i in range(n1):
    L[i] = A[left + i]
  for i in range(n2):
    R[i] = A[mid + i]
  L[n1] = 999999999
  R[n2] = 999999999
  i = 0
  j = 0
  for k in range(left,right):
    cnt+=1
    if L[i] <= R[j]:
      A[k] = L[i]
      i = i + 1
    else:
      A[k] = R[j]
      j = j + 1

def mergeSort(A, left, right):
  #print("margeSort ",A,left,right)
  if left+1 < right:
    mid = int((left + right)/2)
    mergeSort(A, left, mid)
    mergeSort(A, mid, right)
    merge(A, left, mid, right)

n = int(input())
S = list(map(int,input().split()))
mergeSort(S, 0, n)
S = map(str, S)
print(' '.join(S))
print(cnt)