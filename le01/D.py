
if __name__ == "__main__":
    n = int(input())
    R = []
    for i in range(0,n,1):
        R.append(int(input()))
    maxv = R[1] - R[0]
    minv = R[0]
    for i in range(1,n,1):
        maxv = max(maxv, R[i]-minv)
        minv = min(minv,R[i])
    print(maxv)