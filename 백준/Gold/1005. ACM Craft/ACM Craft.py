import collections

t=int(input())

for _ in range(t):
    n,k=map(int,input().split())
    d=[0]+list(map(int,input().split()))
    dp=[d[i] for i in range(n+1)]
    link_cnt=[0 for _ in range(n+1)]
    graph=collections.defaultdict(list)
    for _ in range(k):
        x,y=map(int,input().split())
        graph[x].append(y)
        link_cnt[y]+=1

    target=int(input())
    q=collections.deque()
    for i in range(1,n+1):
        if link_cnt[i]==0:
            q.appendleft(i)

    while q:
        v=q.pop()
        for node in graph[v]:
            link_cnt[node]-=1
            dp[node]=max(dp[node],dp[v]+d[node])
            if link_cnt[node]==0:
                q.appendleft(node)

        if link_cnt[target]==0:
            print(dp[target])
            break


