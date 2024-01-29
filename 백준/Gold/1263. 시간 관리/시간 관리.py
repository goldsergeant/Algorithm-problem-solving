import sys

N=int(sys.stdin.readline())
tasks=[]
for _ in range(N):
    t,s=map(int,sys.stdin.readline().split())
    tasks.append((t,s))

tasks.sort(reverse=True,key=lambda x:(x[1],-x[0]))
start_time=tasks[0][1]-tasks[0][0]
for i in range(1,N):
    cur_dur,cur_end=tasks[i]
    if start_time<cur_end:
        start_time=(cur_end-cur_dur)-(cur_end-start_time)
    else:
        start_time=cur_end-cur_dur

print(start_time if start_time>=0 else -1)

