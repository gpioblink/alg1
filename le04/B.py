# WHATIS: 二分探索　入力はソート済み
n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

def find(key,l,r):
    m = int(l+(r-l)/2)
    #print(str(key) + " " + str(l) + " " + str(m) + " " + str(r))
    if key == S[m]:
        return True
    elif r-l <= 1:
        return False
    elif key < S[m]:
        return find(key,l,m)
    elif key > S[m]:
        return find(key,m+1,r)

cnt = 0
for x in T:
    if find(x,0,n) is True:
        cnt += 1
    
print(cnt)