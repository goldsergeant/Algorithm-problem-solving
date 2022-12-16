s=int(input())
n=0
if s==1 or s==2:
    print(1)
    exit()
for i in range(1,s):
    if n+i>s:
        print(i-1)
        break
    elif n+i==s:
        print(i)
        break
    n+=i