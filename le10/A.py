# WHATIS: フィボナッチ数列の第n項の値を出力する
dp = [0]*5000

def fib(n):
    if dp[n] != 0:
        return dp[n]
    if n==0:
        dp[n] = 1
    elif n==1:
        dp[n] = 1
    else:
        dp[n] = fib(n-1)+fib(n-2)
    return dp[n]

print(fib(int(input())))