import math
def isPrime(x):
    if x==2:
        return True
    
    if x<2 or x%2==0:
        return False
    
    i = 3
    while i <= math.sqrt(x):
        if x%i == 0:
            return False
        i = i+2
    
    return True

if __name__ == "__main__":
    n = int(input())
    a = []
    for l in range(0,n,1):
        a.append(int(input()))
    cnt = 0
    for x in a:
        if isPrime(x):
            cnt += 1
    print(cnt)