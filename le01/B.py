def mygcd(x,y):
    if y != 0:
        mygcd(y,x%y)
    else:
        print(x)

if __name__ == "__main__":
    a,b = map(int,input().split())
    if a<b:
        tmp = a
        a = b
        b = tmp
    mygcd(a,b)
