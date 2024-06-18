import collections
import sys


a1,b1,a2,b2=map(int,sys.stdin.readline().split())
q=collections.deque([(0,0,0)])
visited=set()
while q:
    a,b,cnt=q.popleft()
    if a==a2 and b==b2:
        print(cnt)
        exit()
    if a < a1:  # 물통 채우는 단계
        if (a1,b) not in visited:
            visited.add((a1,b))
            q.append((a1,b,cnt+1))
    if b < b1:
        if (a,b1) not in visited:
            visited.add((a,b1))
            q.append((a,b1,cnt+1))

    if a > 0:  # 물통 버리는 단계
        if (0,b) not in visited:
            visited.add((0,b))
            q.append((0,b,cnt+1))

    if b > 0:
        if (a,0) not in visited:
            visited.add((a,0))
            q.append((a,0,cnt+1))

    if b < b1:  # 물통 옮기는 단계
        if a <= b1 - b:
            if (0,b+a) not in visited:
                visited.add((0,b+a))
                q.append((0,b+a, cnt + 1))
        else:
            if (a-(b1-b),b1) not in visited:
                visited.add((a-(b1-b),b1))
                q.append((a-(b1-b),b1, cnt + 1))
    if a < a1:
        if b <= a1 - a:
            if (a+b,0) not in visited:
                visited.add((a+b,0))
                q.append((a+b,0, cnt + 1))
        else:
            if (a1,b-(a1-a)) not in visited:
                visited.add((a1,b-(a1-a)))
                q.append((a1,b-(a1-a), cnt + 1))

print(-1)