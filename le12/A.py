N = int(input())
V = [-1]*N
L = []
P = []

class  Point:
    def __init__(self,ps,value):
        self.ps = ps
        self.value = value
    def __repr__(self):
        return str(self.ps) + ' ' + str(self.value)

def prim(t,d,c):
    print(t,d,c)
    if c == N:
        return 0
    for i in range(N):
        if L[t][i] != -1 and V[i] == -1:
            P.append(Point(i,L[t][i]))
    print(P)
    min = Point(-1,float('inf'))
    for p in P:
        if V[p.ps] != -1:
            del V[p.ps]
            continue
        if min.value > p.value:
            min = p
    m = Point(min.ps,min.value)
    del min
    V[t] = d
    return m.value + prim(m.ps,m.value, c+1)

    
for i in range(N):
    L.append(list(map(int,input().split())))
print(prim(1,0,0))

