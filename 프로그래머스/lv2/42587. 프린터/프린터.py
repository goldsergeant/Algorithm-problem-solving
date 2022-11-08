def solution(priorities, location):
    result=0
    while priorities:
        if priorities[0]<max(priorities):
            priorities.append(priorities.pop(0))
        else:
            result+=1
            priorities.pop(0)
            if location==0:
                return result
        location-=1
        if location<0:
            location=len(priorities)-1