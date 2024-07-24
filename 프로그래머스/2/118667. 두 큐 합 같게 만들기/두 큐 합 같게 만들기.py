import collections

def solution(queue1, queue2):
    answer = 0
    total1 = sum(queue1)
    total2 = sum(queue2)
    exist_set=set()
    queue1 = collections.deque(queue1)
    queue2 = collections.deque(queue2)

    while total1 != total2:
        if total1 > total2:
            n = queue1.popleft()
            total1 -= n
            queue2.append(n)
            total2 += n
        else:
            n = queue2.popleft()
            total2 -= n
            queue1.append(n)
            total1 += n
        
        left1=0 if not queue1 else queue1[0]
        right1=0 if not queue1 else queue1[-1]
        left2=0 if not queue2 else queue2[0]
        right2=0 if not queue2 else queue2[-1]
        if (total1,total2,left1,right1,left2,right2) in exist_set:
            return -1
        exist_set.add((total1,total2,left1,right1,left2,right2))
        answer += 1
    return answer