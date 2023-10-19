import collections
import heapq
import sys

input=sys.stdin.readline

n=int(input())
if n==0:
    print(0)
    exit()
lecture_dict=collections.defaultdict(list)
answer=0
for _ in range(n):
    p,d=map(int,input().split())
    heapq.heappush(lecture_dict[d],-p)

max_day=max(lecture_dict.keys())
keys=sorted(lecture_dict.keys())
for i in reversed(range(1,max_day+1)):
    selected_day=0
    max_income=0
    for j in reversed(keys):
        if j<i or not lecture_dict[j]:
            continue

        if -lecture_dict[j][0]> -max_income:
            max_income=lecture_dict[j][0]
            selected_day=j
    if selected_day!=0:
        answer-=heapq.heappop(lecture_dict[selected_day])

print(answer)