# WHATIS: 深さ優先探索　方向付き
N = int(input())
L = [[] for i in range(N+1)]
d = [0] * (N+1)
f = [0] * (N+1)

time = 0

def dfs(key):
    global time
    time += 1
    d[key] = time
    for i in range(len(L[key])):
        if d[L[key][i]] == 0:
            dfs(L[key][i])
    time += 1
    f[key] = time
        
for i in range(N):
    Q = list(map(int, input().split()))
    L[Q[0]].extend(Q[2:])

for i in range(1,N+1):
    if d[i] == 0:
        dfs(i)
        #print("done")

for i in range(1,N+1):
    print(i, d[i], f[i])
