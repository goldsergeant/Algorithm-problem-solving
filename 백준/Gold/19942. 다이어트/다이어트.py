import sys

n=int(sys.stdin.readline())
mp,mf,ms,mu=map(int,sys.stdin.readline().split())
answer=[]
nutrition_info=[]
for _ in range(n):
    nutrition_info.append(list(map(int,sys.stdin.readline().split())))

def dfs(p,f,s,u,c,numbers,node):
    if p>=mp and f>=mf and s>=ms and u>=mu:
        answer.append((c,numbers))
        return

    for i in range(node+1,n):
        dfs(p+nutrition_info[i][0],f+nutrition_info[i][1],s+nutrition_info[i][2],u+nutrition_info[i][3],c+nutrition_info[i][4],numbers+[i+1],i)

for i in range(n):
    dfs(nutrition_info[i][0],nutrition_info[i][1],nutrition_info[i][2],nutrition_info[i][3],nutrition_info[i][4],[i+1],i)

answer.sort()
if answer:
    print(answer[0][0])
    print(*answer[0][1])
else:
    print(-1)