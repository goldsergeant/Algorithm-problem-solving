import sys

n,m=map(int,sys.stdin.readline().split())
readline=sys.stdin.readline().rstrip()
truth_count=int(readline[0])
truth_people=[]
coming_people=[]
answer=0
parent=[0]+[i for i in range(1,n+1)]

for _ in range(m):
    coming_people.append(list(map(int,sys.stdin.readline()[2:].split())))

def find(x):
    if x!=parent[x]:
        return find(parent[x])
    return x

def union(a,b):
    a=find(a)
    b=find(b)
    if a in truth_people and b in truth_people:
        return
    elif a in truth_people:
        parent[b]=a
    elif b in truth_people:
        parent[a]=b
    else:
        if a<b:
            parent[b]=a
        else:
            parent[a]=b

if truth_count!=0:
    truth_people=list(map(int, readline[2:].split()))

for cur_people in coming_people:
    for i in range(len(cur_people)-1):
        union(cur_people[i],cur_people[i+1])

for cur_people in coming_people:
    flag=0
    for i in range(len(cur_people)):
        if find(cur_people[i]) in truth_people:
            flag=1
            break
    if flag==0:
        answer+=1

print(answer)