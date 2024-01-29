import sys

N=int(sys.stdin.readline())
tasks=[]
for _ in range(N):
    t,s=map(int,sys.stdin.readline().split())
    tasks.append((s-t,s))

tasks.sort(reverse=True,key=lambda x:(x[1],x[0]))
start_time=tasks[0][0]
for i in range(1,N):
    cur_start,cur_end=tasks[i]
    if start_time<cur_end:
        start_time=cur_start-(cur_end-start_time)
    else:
        start_time=cur_start

print(start_time if start_time>=0 else -1)

