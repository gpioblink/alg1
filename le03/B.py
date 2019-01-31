queue = []
head = 0
tail = 0
cnt = 0
MAX = 1000000
def enqueue(x):
    global tail
    global MAX
    queue[tail] = x
    tail += 1
    if tail == MAX:
        tail = 0


def dequeue():
    global head
    global MAX
    x = queue[head]
    head += 1
    if head == MAX:
        head = 0
    return x


queue.extend(range(0,MAX+1,1))
n, q = list(map(int,input().split()))
for i in range(0,n,1):
    idata, value = input().split()
    value = int(value)
    enqueue((idata,value))

while head!=tail:
    #print(queue)
    idata, value = dequeue()
    value -= q
    cnt += min(q,value+q)
    if value<=0:
        print(idata+" "+str(cnt)) 
        continue   
    enqueue((idata,value))