n = int(input())
M = []
dp = [[None for i in range(10)] for i in range(10)]

def calcMatrix(i,j):
    print(i,j)
    if i == j:
        dp[i][j] = 0
    elif i == j-1:
        dp[i][j] = M[i-1]*M[i]*M[i+1]
    else:
        for k in range(i-j):
            print(i,j,k)
            print(dp[i][i+k])
            print(dp[i+k][j])
            current = dp[i][i+k] + dp[i+k][j] + M[i-1] * M[i+k+1] * M[j+1]
            if k==0:
                dp[i][j] = current
            if current < dp[i][j]:
                dp[i][j] = current 





for i in range(n-1):
    Q = list(map(int,input().split()))
    M.append(Q[0])
Q = list(map(int,input().split()))
M.append(Q[0])
M.append(Q[1])
print(M)

for i in range(n):
    for j in range(n-i):
        calcMatrix(i+j,j)
        for k in range(10):
         print(dp[k])
        print()
print(dp[0][n-1])