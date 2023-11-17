import sys

n=int(sys.stdin.readline())
loss_arr=list(map(int,sys.stdin.readline().split()))
joy_arr=list(map(int,sys.stdin.readline().split()))
answer=0
health=100
def dfs(idx,health,total_joy):
    global answer
    if idx>=n-1:
        answer = max(answer, total_joy)
        return

    if health-loss_arr[idx+1]>0:
        dfs(idx+1,health-loss_arr[idx+1],total_joy+joy_arr[idx+1])
    dfs(idx+1,health,total_joy)

dfs(0,100,0)
if health-loss_arr[0]>0:
    dfs(0,health-loss_arr[0],joy_arr[0])
print(answer)
