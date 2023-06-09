N,L =map(int,input().split())
pools=[]
answer=0

for _ in range(N):
    start,end=map(int,input().split())
    pools.append((start, end))

pools.sort(key=lambda x:x[0])

i=0
cur=pools[0][0]
while i<len(pools):
    if cur<pools[i][0]:
        cur=pools[i][0]

    while cur<pools[i][1]:
        cur+=L
        answer+=1

    i+=1

print(answer)
