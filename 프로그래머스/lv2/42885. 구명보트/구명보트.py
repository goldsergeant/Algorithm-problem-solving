import collections
def solution(people, limit):
    people.sort(reverse=True)
    deq=collections.deque(people)
    reps=0
    while deq:
        current_limit=limit-deq.popleft()
        while deq and deq[-1]<=current_limit:
            current_limit-=deq.pop()
        reps+=1
    return reps
    