import heapq

n,m=map(int,input().split())
answer=0
arr_of_milieages=[]
for _ in range(n):
    p,l=map(int,input().split())
    mileages=list(map(int,input().split()))
    mileages.sort()

    if l-p>0:
        heapq.heappush(arr_of_milieages, (1, mileages))

    elif p-l>len(mileages)-1:
        heapq.heappush(arr_of_milieages,(mileages[-1],mileages))
    else:
        heapq.heappush(arr_of_milieages,(mileages[max(0,p-l)],mileages))

while arr_of_milieages:
    mileage=heapq.heappop(arr_of_milieages)[0]
    if m>=mileage:
        answer+=1
        m-=mileage
    else:
        break


print(answer)
