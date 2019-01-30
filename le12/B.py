N = int(input())
L = [[float('inf')]*N for i in range(N)]


def dijkstra(s):
    S = set()
    d = [float('inf')] * N
    d[s] = 0
    p = [None]*N

    while len(S) != N:
        minv = float('inf')
        u = None
        for i in range(N):
            if d[i] < minv and i not in S:
                u = i
                minv = d[i]
        S.add(u)
        for u in S:
            for v in range(N):
                if d[u] + L[u][v] < d[v] and v not in S:
                    d[v] = d[u] + L[u][v]
                    p[v] = u

    for i in range(N):
        print('{} {}'.format(i, d[i]))
        # print(S)


for i in range(N):
    Q = list(map(int, input().split()))
    for j in range(Q[1]):
        L[Q[0]][Q[2+2*j]] = Q[3+2*j]
dijkstra(0)
