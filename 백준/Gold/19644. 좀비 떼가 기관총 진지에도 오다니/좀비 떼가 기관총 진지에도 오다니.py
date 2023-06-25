import collections
import sys

L=int(input())
Ml,Mk=map(int,input().split())
C=int(input())
zombies=[int(sys.stdin.readline().rstrip()) for _ in range(L)]
answer=True
queue=collections.deque()
use_bomb=0

for i in range(min(Ml,L)): #처음 큐에 넣기
    if use_bomb==0:
        expect_zombie_health=zombies[i]-Mk*(i+1)
        if expect_zombie_health<=0:
            queue.append(0)
        else:
            queue.append(expect_zombie_health)
            use_bomb+=1

    else:
        expect_zombie_health=zombies[i]-Mk*(i+1-use_bomb)
        if expect_zombie_health<=0:
            queue.append(0)
        else:
            queue.append(expect_zombie_health)
            use_bomb+=1

for i in range(Ml,L):
    first_zombie=queue.popleft()
    if first_zombie==0:
        if zombies[i]-Mk*(Ml-use_bomb)<=0:
            queue.append(0)
        else:
            queue.append(zombies[i]-Mk*(Ml-use_bomb))
            use_bomb+=1

    else:
        if C>0:
            C-=1
        else:
            answer=False
            break
        if zombies[i]-Mk*(Ml-use_bomb)<=0:
            queue.append(0)
            use_bomb-=1
        else:
            queue.append(zombies[i]-Mk*(Ml-use_bomb))

if answer:
    while queue:
        first_zombie=queue.popleft()

        if first_zombie==0:
            continue
        else:
            if C>0:
                C-=1
            else:
                answer=False
                break
print('YES' if answer else 'NO')