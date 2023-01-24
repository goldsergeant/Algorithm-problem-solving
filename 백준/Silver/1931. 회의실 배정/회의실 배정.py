n=int(input())
meetings=[]
cur=0
count=1
for _ in range(n):
    meetings.append(tuple(map(int,input().split())))
meetings.sort(key=lambda x:x[0])
meetings.sort(key=lambda x:x[1])

for i in range(1,n):
    if meetings[cur][1]<=meetings[i][0]:
        count+=1
        cur=i
    else:
        continue

print(count)