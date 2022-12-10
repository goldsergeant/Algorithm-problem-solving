import itertools

def solution(k, dungeons):
    result = []
    indexes = list(itertools.permutations(dungeons))
    for i in range(len(indexes)):
        answer = 0
        remain =k
        for j in range(len(indexes[i])):
            if remain>= indexes[i][j][0]:
                answer+=1
                remain-=indexes[i][j][1]
        result.append(answer)

    return max(result)
