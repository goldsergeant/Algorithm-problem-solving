import sys

n=int(input())
numbers=[]
for _ in range(n):
    s=sys.stdin.readline().rstrip()
    tmp=''
    for i in range(len(s)):
        if s[i].isdigit():
            tmp+=s[i]
        else:
            if len(tmp)>0:
                numbers.append(int(tmp))
            tmp=''
    if len(tmp)>0:
        numbers.append(int(tmp))

numbers.sort()
for num in numbers:
    print(num)
