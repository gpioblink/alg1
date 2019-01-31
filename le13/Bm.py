N = 3
M = 3
board = []
expected = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

queue = []
bqueue = []

history = []

def swap(x1, y1, x2, y2, b):
    # 2次元配列を浅いコピーするなんて
    t = [x[:] for x in b]
    t[x1][y1], t[x2][y2] = t[x2][y2], t[x1][y1]
    return t


def bfs():
    if expected == board:
        print(0)
        exit(0)

    while len(queue):
        # print(queue)
        # print(bqueue)
        pazzle = queue[0]
        del queue[0]
        cost = bqueue[0]
        del bqueue[0]
        # 0の場所を探す
        xz = None
        yz = None
        for i in range(N):
            for j in range(M):
                if pazzle[i][j] == 0:
                    xz, yz = i, j
        # 動かすことのできる方向を全て調べる
        xm = [1, 0, 0, -1]
        ym = [0, -1, 1, 0]
        for k in range(4):
            if 0 <= xz + xm[k] < N and 0 <= yz + ym[k] < N:
                # １手動かしてあったら終了。なかったら次の手に行く。
                t = swap(xz, yz, xz + xm[k], yz + ym[k], pazzle)
                if expected == t:
                    print(cost+1)
                    exit(0)
                # 今までに出てないならキューに追加
                if t not in history:
                    queue.append(t)
                    history.append(t)
                    bqueue.append(cost+1)


for i in range(N):
    board.append(list(map(int, input().split())))
queue.append(board)
bqueue.append(0)
bfs()