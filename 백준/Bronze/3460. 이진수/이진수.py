t=int(input())
for _ in range(t):
    n=int(input())
    st=bin(n)[::-1]
    for index,char in enumerate(st[:-2]):
        if char =="1":
            print(index,end=" ")
