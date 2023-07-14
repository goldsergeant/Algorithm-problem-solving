import sys

target=input()
n=int(input())
answer=0
for _ in range(n):
    st=sys.stdin.readline().rstrip()
    for i in range(len(st)):
        tmp=''
        for j in range(i,i+len(target)):
            tmp+=st[j%len(st)]
        if tmp==target:
            answer+=1
            break

print(answer)
