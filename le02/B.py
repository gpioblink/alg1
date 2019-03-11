# WHATIS: 選択ソート 安定でない
N = int(input())
A = list(map(int, input().split(' ')))

flag = 1 #一度でも入れ替えをした
cnt = 0
point = 0
while point < N:
    rpoint = point
    for i in range(point,N,1):
        if A[rpoint] > A[i]:
            rpoint = i
    A[point], A[rpoint] = A[rpoint], A[point]
    if point != rpoint:
        cnt += 1
    point += 1

print (' '.join(map(str,A)))
print(cnt)

