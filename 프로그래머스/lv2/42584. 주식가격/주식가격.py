import collections
def solution(prices):
    que=collections.deque(prices)
    answer=[]
    while que:
        current_price=que.popleft()
        count=0
        for price in que:
            count+=1
            if price<current_price:
                break
        answer.append(count)
    return answer