def printHeap(H,Q,n):
    if H+1 == n:
        return
    print("node",n,end=": ")
    print("key =",Q[n],end=", ")
    print("parent key =",Q[int(n/2)],end=", ") if 1<n else None
    print("left key =",Q[2*n],end=", ") if 2*n<=H else None
    print("right key =",Q[2*n+1],end=", ") if 2*n+1<=H else None
    print()
    printHeap(H,Q,n+1)
    



H = int(input())
Q = list(map(int, input().split()))
Q.insert(0,-1)
printHeap(H,Q,1)

