x,y=map(int,input().split())
z=(y*100)//x
low=0
high=1000000000
if z>=99:
    print(-1)
    exit()

while low<=high:
    mid=(low+high)//2
    temp_z=((y+mid)*100)//(x+mid)

    if temp_z>z:
        high=mid-1
    else:
        low=mid+1
        answer=mid+1

print(low)