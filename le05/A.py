
def selectWhich(A,i,c):
    #print(A)
    #print(i)
    #print(c)
    if c < 1:
        return
    if int(i/c) == 1:
        A.append(1)
        i = i%c
    else:
        A.append(0)
    selectWhich(A,i,c/2)


n = int(input())
A = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))
p = []

for i in range(2**n):
    l = []
    selectWhich(l,i,2**n)
    tmp = [ x*y for (x,y) in zip(A,l[1:])]
    p.append(sum(tmp))
#print(p)
for query in m:
    #flag = False
    #for d in p:
    #    if(query==d):
    #        flag = True
    #        break
    if query in p:
        print("yes")
    else:
        print("no")