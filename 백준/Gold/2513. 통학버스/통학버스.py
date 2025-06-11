import collections
import math
import sys

N,K,S=map(int,sys.stdin.readline().split())
students=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
left_students=[]
right_students=[]

for i in range(N):
    if students[i][0]<S:
        left_students.append((S-students[i][0],students[i][1]))
    else:
        right_students.append((students[i][0]-S,students[i][1]))

left_students=collections.deque(sorted(left_students,reverse=True))
right_students=collections.deque(sorted(right_students,reverse=True))

def service(q):
    answer=0
    left = K
    max_dist=0
    while q:
        dist,num=q.popleft()
        max_dist=max(max_dist,dist)
        if left<num:
            answer+=max_dist*2
            q.appendleft((dist,num-left))
            max_dist=0
            left=K
        else:
            left-=num


    return answer+max_dist*2

print(service(left_students)+service(right_students))