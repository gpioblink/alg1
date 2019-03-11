# WHATIS: バブルソート

N = int(input())
A = list(map(int, input().split(' ')))

flag = 1 #一度でも入れ替えをした
cnt = 0
while flag:
    flag = 0
    for i in range(1,N,1):
        if A[i-1] > A[i]:
            A[i-1], A[i] = A[i], A[i-1]
            cnt += 1
            flag = 1
print (' '.join(map(str,A)))
print(cnt)


