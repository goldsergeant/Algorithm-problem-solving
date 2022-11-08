import sys
def solution(routes):
    routes.sort(key=lambda x:x[1])
    answer=0
    camera=-sys.maxsize
    for i in range(len(routes)):
        if routes[i][0]>camera:
            answer+=1
            camera=routes[i][1]
    print(routes)
    return answer