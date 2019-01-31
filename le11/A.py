N = int(input())
L = [[0]*(N+1) for i in range(N+1)]
for i in range(N):
    D = list(map(int, input().split()))
    for j in range(2,len(D)):
        L[D[0]][D[j]] = 1
for i in range(1,N+1):
    print(' '.join(map(str,L[i][1:])))