import sys

N=int(input())
arr=list(map(int,sys.stdin.readline().split()))
opt=list(map(int,sys.stdin.readline().split()))
answer=[]

def dfs(idx,num):
    if idx==N-1:
        answer.append(num)
        return

    for i in range(4):
        if opt[i]>0:
            opt[i]-=1
            if i==0:
                dfs(idx+1,num+arr[idx+1])
            elif i==1:
                dfs(idx+1,num-arr[idx+1])
            elif i == 2:
                dfs(idx + 1, num * arr[idx + 1])
            elif i == 3:
                if num<0:
                    dfs(idx+1,-(-num//arr[idx+1]))
                else:
                    dfs(idx + 1, num // arr[idx + 1])

            opt[i]+=1

dfs(0,arr[0])
print(max(answer))
print(min(answer))
