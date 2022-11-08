def solution(progresses, speeds):
    result=[]
    while progresses:
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        reps=0
        while progresses and progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            reps+=1
        if reps!=0:
            result.append(reps)
    return result