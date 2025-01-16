import sys

sys.setrecursionlimit(1000000)
def solution(k, room_number):
    parent=dict()
    answer = []

    def find(x):
        if parent.get(x,x)!=x:
            parent[x]=find(parent.get(x,x))
        return parent.get(x,x)

    def union(a,b):
        a=find(a)
        b=find(b)
        parent[a] = parent.get(b,b)

    for n in room_number:
        n=find(n)
        answer.append(n)
        union(n,n+1)

    return answer