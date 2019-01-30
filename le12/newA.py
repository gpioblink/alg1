N = int(input())
L = []  # input


def prim():
    # 頂点を適当に選ぶ
    s = None
    for i in range(N):
        for j in range(N):
            if L[i][j] != -1:
                s = i
                break
        if s is not None:
            break
    p = {s}
    T = []
    k = 0
    while k < N - 1:
        # 最終のP内で一番短いやつを加える
        len = float("inf")
        lenside = []
        for sg in p:
            for i in range(N):
                isT = False
                for t in T:
                    if (t[0] == sg and t[1] == i) or (t[0] == i and t[1] == sg):
                        # print("ignore")
                        isT = True
                        continue
                #注意 i not in p を忘れて
                if isT is False and i not in p and L[sg][i] != -1 and L[sg][i] < len:
                    len = L[sg][i]
                    lenside = [sg, i]

        p.add(lenside[0])
        p.add(lenside[1])
        T.append(lenside)
        k = k + 1
        #print(p,T,k)
    cnt = 0
    for t in T:
        cnt += L[t[0]][t[1]]
    print(cnt)


for i in range(N):
    L.append(list(map(int, input().split())))
prim()