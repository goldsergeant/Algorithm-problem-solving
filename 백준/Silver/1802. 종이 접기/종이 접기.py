import sys

T=int(input())

def dfs(st,left,right):
    global is_can_fold
    mid= (right+left)//2
    if left==right:
        return st[left:right+1]

    left_st=dfs(st,left,mid-1)
    right_st=dfs(st,mid+1,right)[::-1]
    for i in range(len(left_st)):
        if left_st[i]==right_st[i]:
            is_can_fold=False

    return st[left:right+1]


is_can_fold=True

for _ in range(T):
    is_can_fold=True
    paper=sys.stdin.readline().rstrip()

    dfs(paper,0,len(paper)-1)

    print('YES' if is_can_fold else 'NO')
