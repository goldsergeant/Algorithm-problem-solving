N=int(input())
sliding=sorted(list(map(int,input().split())),reverse=True)
for _ in range(N-1):
    arr=sorted(list(map(int,input().split())),reverse=True)

    arr_idx=0
    sliding_idx=0
    tmp=[]

    for _ in range(N):
        num1,num2=arr[arr_idx],sliding[sliding_idx],
        if num1>num2:
            tmp.append(num1)
            arr_idx+=1
        else:
            tmp.append(num2)
            sliding_idx+=1

    sliding=tmp

print(sliding[-1])