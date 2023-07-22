import sys

n=int(input())
answer=0
for _ in range(n):
    st=sys.stdin.readline().rstrip()
    visited=[st[0]]
    flag=0
    for i in range(1,len(st)):
        if st[i]!=st[i-1] and st[i] in visited:
            flag=1

        if st[i] not in visited:
            visited.append(st[i])
    if flag==0:
        answer+=1
print(answer)