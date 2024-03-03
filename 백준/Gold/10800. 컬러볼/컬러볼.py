import collections
import sys
N=int(sys.stdin.readline())
balls=[]
answer=[0 for _ in range(N)]
color_dict=collections.defaultdict(int)
for i in range(N):
    color,size=map(int,sys.stdin.readline().split())
    balls.append((i,color,size))

balls.sort(key=lambda x:(x[2],x[1]))

cur=0
j=0
for i in range(len(balls)):
    while balls[j][2]<balls[i][2]:
        cur+=balls[j][2]
        color_dict[balls[j][1]]+=balls[j][2]
        j+=1

    answer[balls[i][0]]=cur-color_dict[balls[i][1]]

for n in answer:
    print(n)