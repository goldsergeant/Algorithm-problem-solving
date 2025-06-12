import sys

N,K,S=map(int,sys.stdin.readline().split())
left_students=[]
right_students=[]

def service(arr:list):
    max_dist=0
    result=0
    left=K
    while arr:
        point,cnt=arr[-1]
        max_dist=max(max_dist,point)
        if cnt<=left:
            arr.pop()
            left-=cnt
        else:
            arr[-1][1] -= left
            left=K
            result+=max_dist*2
            max_dist=0

    result+=max_dist*2
    return result

for _ in range(N):
    point,cnt=map(int,sys.stdin.readline().split())
    if point<S:
        left_students.append([S-point,cnt])
    else:
        right_students.append([point-S,cnt])

left_students.sort()
right_students.sort()

print(service(left_students)+service(right_students))
