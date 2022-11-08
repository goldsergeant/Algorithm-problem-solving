def solution(brown, yellow):
    answer = []
    for i in range(1,brown+yellow+1):
        if (brown+yellow)%i==0:
            answer.append(((brown+yellow)//i,i))
    answer.sort(key=lambda x:abs(x[0]-x[1]))
    for i in answer:
        if (i[0]-2)*(i[1]-2)==yellow:
            return i