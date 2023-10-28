import collections
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())
left = 0
right = 1
tree = collections.defaultdict(list)
parent = [i for i in range(n+1)]
visited = [False] * (n + 1)
answer=-1
for _ in range(n):
    root, a, b = map(int, input().split())
    tree[root].append(a)
    tree[root].append(b)
    if a!=-1:
        parent[a]=root
    if b!=-1:
        parent[b]=root

def get_end_inorder():
    visited_node=[]
    def inorder(node):
        if tree[node][left]!=-1:
            inorder(tree[node][left])
        visited_node.append(node)
        if tree[node][right]!=-1:
            inorder(tree[node][right])

    inorder(1)
    return visited_node[-1]

end_node=get_end_inorder()
def similar_inorder(node):
    global answer,end_node
    visited[node] = True
    answer+=1

    if tree[node][left] != -1 and not visited[tree[node][left]]:
        visited[tree[node][left]]=True
        similar_inorder(tree[node][left])
    elif tree[node][right]!=-1 and not visited[tree[node][right]]:
        visited[tree[node][right]]=True
        similar_inorder(tree[node][right])
    elif node==end_node:
        return
    elif node!=parent[node]:
        similar_inorder(parent[node])

similar_inorder(1)
print(answer)