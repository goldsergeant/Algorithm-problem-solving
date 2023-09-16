import collections
import sys

t=int(input())

def oper_d(num):
    return 2*num%10000

def oper_s(num):
    return 9999 if num==0 else num-1

def oper_l(num):
    fourth_num=num//1000
    other_num=num%1000
    return other_num*10+fourth_num

def oper_r(num):
    first_num=num%10
    other_num=(num-first_num)//10
    return first_num*1000+other_num
def bfs(start,target):
    visited=[False for _ in range(10000+1)]
    visited[start]=True
    q=collections.deque()
    q.appendleft((start,''))
    while q:
        cur_num,command=q.pop()
        if cur_num==target:
            return command
        d=oper_d(cur_num)
        if not visited[d]:
            visited[d]=True
            q.appendleft((d,command+'D',))

        s=oper_s(cur_num)
        if not visited[s]:
            visited[s]=True
            q.appendleft((s,command+'S',))

        r = oper_r(cur_num)
        if not visited[r]:
            visited[r]=True
            q.appendleft((r,command+'R'))

        l=oper_l(cur_num)
        if not visited[l]:
            visited[l]=True
            q.appendleft((l,command+'L',))





for _ in range(t):
    a,b=map(int,input().split())
    print(bfs(a,b))