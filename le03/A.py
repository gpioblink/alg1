stack = []
top = 0
def push(a):
    global top
    stack[top] = a
    top += 1 

def pop():
    global top
    top -= 1
    return stack[top]


if __name__ == '__main__':
    stack.extend(range(0,10000,1))
    s = str(input()).split()
    for c in s:
        #print(stack)
        if c == '+':
            push((pop())+pop())
        elif c == '-':
            push((-pop())+pop())
        elif c == '*':
            push(pop()*pop())
        else:
            push(int(c))
    print(pop())