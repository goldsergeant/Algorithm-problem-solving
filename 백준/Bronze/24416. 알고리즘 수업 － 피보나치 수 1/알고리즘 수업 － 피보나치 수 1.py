recur=0
dynamic=0

def fib(n):
    if n==1 or n==2:
        global recur
        recur += 1
        return 1
    return fib(n-1)+fib(n-2)

def fibonacci(n):
    f=[0 for i in range(n+1)]
    f[1]=f[2]=1
    for i in range(3,n+1):
        f[i]=f[i-1]+f[i-2]
        global dynamic
        dynamic+=1
    return f[n]

n=int(input())
fib(n)
fibonacci(n)
print(recur)
print(dynamic)
