import sys

T=int(sys.stdin.readline())
for _ in range(T):
    arr=list(map(int,sys.stdin.readline().split()))
    t=arr[0]
    arr=arr[1:]
    max_height=0
    answer=0
    tmp=[]
    for height in arr:
        if not tmp or height>tmp[-1]:
            tmp.append(height)
        else:
            idx=0
            for i in range(len(tmp)-1,-1,-1):
                if tmp[i]<height:
                    idx=i+1
                    break
            tmp.insert(idx,height)
            answer+=len(tmp)-idx-1
    print(t,answer)