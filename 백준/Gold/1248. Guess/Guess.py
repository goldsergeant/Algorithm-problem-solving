n=int(input())
matrix=list(input())

s=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i,n):
        temp=matrix.pop(0)
        if temp=='+':
            s[i][j]=1
        elif temp=='-':
            s[i][j]=-1

def check(answer:list) -> bool:
    check_num=0
    idx=len(answer)-1
    for i in range(idx,-1,-1):
        check_num+=answer[i]
        if check_num<0 and s[i][idx]>=0:
            return False

        elif check_num>0 and s[i][idx]<=0:
            return False
        elif check_num==0 and s[i][idx]!=0:
            return False
    return True


def dfs(answer:list):
    if len(answer)==n:
        print(' '.join(map(str,answer)))
        exit()

    if s[len(answer)][len(answer)]==0: #대각선이 0일때
        dfs(answer+[0])
        return

    for i in range(1,11):
        temp_num=s[len(answer)][len(answer)]*i
        if check(answer+[temp_num]):
            dfs(answer+[temp_num])

dfs([])
