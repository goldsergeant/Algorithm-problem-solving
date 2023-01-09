import sys

n=int(input())
people=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    people.append([x,y,1])

for i in range(n):
    for j in range(n):
        if i!=j:
            if people[i][0]<people[j][0] and people[i][1]<people[j][1]:
                people[i][2]+=1

print(' '.join(str(i[2]) for i in people))
