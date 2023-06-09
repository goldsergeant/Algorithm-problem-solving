N,L =map(int,input().split())
pools=[]
answer=0

for _ in range(N):
    start,end=map(int,input().split())
    pools.append((start, end))

pools.sort(key=lambda x:x[0])
end=0
for i in range(N):
    if pools[i][1]<end:
        continue

    start=max(end,pools[i][0])
    d=pools[i][1]-start
    answer+=d//L
    if d%L==0:
        end=pools[i][1]
    else:
        answer+=1
        end=pools[i][1]+(L-(d%L))

print(answer)
