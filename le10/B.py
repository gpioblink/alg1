# WHATIS: 連鎖行列積 行列で掛け算の回数が最小になるときの計算数算出
n = int(input())
M = []
dp = [[None for i in range(100)] for i in range(100)]

def calcMatrix(i,j):
    #print(i,j)
    if i == j:
        dp[i][j] = 0
    elif i == j-1:
        dp[i][j] = M[i]*M[i+1]*M[i+2]
    else:
        for k in range(j-i):
            #print(i,j,k)
            #print(dp[i][i+k])
            #print(dp[i+k+1][j])
            #print(M[i]*M[k+1]*M[j])
            current = dp[i][i+k] + dp[i+k+1][j] + M[i]*M[i+k+1]*M[j+1]
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
#print(M)

for i in range(n):
    for j in range(n-i):
        calcMatrix(j,i+j)
        #for k in range(10):
        # print(dp[k])
        # print()
print(dp[0][n-1]) 