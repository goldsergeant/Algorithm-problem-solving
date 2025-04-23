import collections
import sys
sys.setrecursionlimit(1000000)

N=int(sys.stdin.readline())
scores=[0]+list(map(int,sys.stdin.readline().split()))
parent=[0,0]+list(map(int,sys.stdin.readline().split()))
tree=collections.defaultdict(list)
dp=[[-sys.maxsize,-sys.maxsize] for _ in range(N+1)]
for i in range(2,N+1):
    tree[parent[i]].append(i)

def get_attend_nodes(node,is_attended_parent,attend_nodes):
    if is_attended_parent:
        for child in tree[node]:
            get_attend_nodes(child,False,attend_nodes)
    else:
        if dp[node][0]>dp[node][1] or node==1:
            attend_nodes.append(node)
            for child in tree[node]:
                get_attend_nodes(child,True,attend_nodes)
        else:
            for child in tree[node]:
                get_attend_nodes(child,False,attend_nodes)

def dfs(node):
    dp[node]=[scores[node],0]
    attend=dp[node][0]
    not_attend=dp[node][1]

    for child in tree[node]:
        c_attend,c_not_attend=dfs(child)
        attend=max(attend,attend+c_not_attend)
        not_attend=max(not_attend,not_attend+c_attend,not_attend+c_not_attend)

    dp[node][0]=attend
    dp[node][1]=not_attend
    return dp[node]

print(*dfs(1))
root_attended_nodes=[]
root_not_attended_nodes=[]
get_attend_nodes(1,False,root_attended_nodes)
get_attend_nodes(1,True,root_not_attended_nodes)
print(*(sorted(root_attended_nodes)+[-1]))
print(*(sorted(root_not_attended_nodes)+[-1]))