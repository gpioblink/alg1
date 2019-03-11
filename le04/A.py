# WHATIS: 線形探索　数列SとTから含まれるものの個数
n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))
#print(T)
cnt = 0
for x in T:
    for q in S:
        #print(str(x) + " " + str(q))
        if x==q:
            cnt += 1
            break
            
print(cnt)