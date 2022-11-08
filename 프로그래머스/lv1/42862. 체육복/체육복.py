def solution(n, lost, reserve):
    i=0
    lost.sort()
    reserve.sort()
    reserve,lost=list(set(reserve)-set(lost)),list(set(lost)-set(reserve))

    while i<len(reserve):
        if reserve[i]-1 in lost:
            lost.remove(reserve[i]-1)
            reserve.pop(i)
        elif reserve[i]+1 in lost:
            lost.remove(reserve[i]+1)
            reserve.pop(i)
        else:
            i+=1
    n-=len(lost)
    return n    