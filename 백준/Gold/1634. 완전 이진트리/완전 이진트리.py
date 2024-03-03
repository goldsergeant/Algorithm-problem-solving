import sys

N = int(sys.stdin.readline())
T1 = list(map(int, sys.stdin.readline().split()))
T2 = list(map(int, sys.stdin.readline().split()))

def dfs(l1,r1,l2,r2 ,depth):
    if depth==N:
        return 1 if T1[l1]==T2[l2] else 0

    mid1=(l1+r1)//2
    mid2=(l2+r2)//2

    original=dfs(l1,mid1,l2,mid2,depth+1)+dfs(mid1+1,r1,mid2+1,r2,depth+1)
    reverse=dfs(mid1+1,r1,l2,mid2,depth+1)+dfs(l1,mid1,mid2+1,r2,depth+1)

    return max(original,reverse)

print(dfs(0,len(T1)-1,0,len(T2)-1,1))
