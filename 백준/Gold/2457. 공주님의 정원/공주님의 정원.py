import collections
import sys

N = int(sys.stdin.readline())
flowers = []
end_date=301
answer=0
for i in range(N):
    a,b,c,d=sys.stdin.readline().split()
    a,b,c,d=map(lambda x:x.zfill(2),[a,b,c,d])
    flowers.append(list(map(int,(a+b,c+d))))

flowers.sort()
flowers=collections.deque(flowers)
while flowers:
    if end_date>=1201 or flowers[0][0]>end_date:
        break

    temp_end_date=0
    for _ in range(len(flowers)):
        if flowers[0][0]<=end_date:
            temp_end_date=max(temp_end_date,flowers[0][1])
            flowers.popleft()
        else:
            break
    answer+=1
    end_date=max(end_date,temp_end_date)

print(answer if end_date>1131 else 0)
