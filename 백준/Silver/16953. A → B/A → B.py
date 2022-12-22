a,b=map(int,input().split())
answer=[]
def dfs(num,depth):
    if num==b:
        answer.append(depth)
        return
    elif num>b:
        return
    elif num<b:
        dfs(int(str(num)+"1"),depth+1)
        dfs(num*2,depth+1)
dfs(a,0)
print(min(answer)+1 if len(answer)>0 else -1)