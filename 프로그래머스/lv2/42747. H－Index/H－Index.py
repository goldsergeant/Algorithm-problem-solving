def solution(citations):
    citations.sort(reverse=True)
    answer=0
    for i in range(len(citations)):
        if i>=citations[i]:
            return i
    return len(citations)