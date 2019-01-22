class Node:
    def __init__(self,key,left,right,parent):
        self.key = key
        self.left = left
        self.right = right
        self.p = parent

    def __repr__(self):
        return str(self.key)

def insert(T, z):
    y = None
    x = T 
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    #print(x,y,z)
    if y == None:
        #print("Y==None")
        T = z
        print(T)
    elif z.key<y.key:
        #print("z.key<y.key")
        y.left = z
    else:
        #print("z.key<y.key")
        y.right = z

def find(T, k, show):
    x = T 
    while x != None:
        if k == x.key:
            if show:
                print('yes')
            return x
        if k < x.key:
            x = x.left
        else:
            x = x.right
    print('no')
    
def delete(T,x):
    #print(x.key, id(x))
    if x.left == x.right == None:
        #print("x.left == x.right == None")
        if x.p.key < x.key:
            x.p.right = None
        else:
            x.p.left = None

    elif x.left == None:
        #print("x.left == None")
        y = x.right
        x.key = y.key
        x.right = y.right
        x.left = y.left
        #print(x.key, id(x))
    elif x.right == None:
        #print("x.right == None")
        y = x.left
        x.key = y.key
        x.right = y.right
        x.left = y.left
        #print(x.key, id(x))
    else:
        #print("else")
        x.key = x.left.key
        delete(T, x.left)


    

def printPreorder(x):
    if x == None:
        return
    printPreorder(x.left)
    print(end=' ')
    print(x,end='')
    printPreorder(x.right)

def printMidorder(x):
    if x == None:
        return
    print(end=' ')
    print(x,end='')
    printMidorder(x.left)
    printMidorder(x.right)

def printal(x):
    printPreorder(x)
    print()
    printMidorder(x)
    print()


N = int(input())
Q = input().split()
T = Node(int(Q[1]),None,None,None)
for i in range(N-1):
    Q = input().split()
    if Q[0] == "print":
        printal(T)
        continue
    elif Q[0] == "find":
        find(T,int(Q[1]),True)
        continue
    elif Q[0] == "delete":
        delete(T,find(T, int(Q[1]), False))
        continue
    insert(T,Node(int(Q[1]),None,None,None))
