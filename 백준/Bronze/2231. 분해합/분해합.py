n=int(input())
for i in range(1,n):
    num=0
    for char in str(i):
        num+=int(char)
    if i+num==n:
        print(i)
        exit()
print(0)