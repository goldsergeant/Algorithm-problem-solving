import collections
def solution(bridge_length, weight, truck_weights):
    queue=collections.deque()
    t_queue=collections.deque()
    time=0
    while True:
        time+=1
        for i in range(len(t_queue)):
            t_queue[i]-=1
            if t_queue[i]==0:
                queue.pop()
                t_queue.pop()
        if truck_weights and sum(queue)+truck_weights[0]<=weight:
            queue.appendleft(truck_weights.pop(0))
            t_queue.appendleft(bridge_length)
        if not queue and not truck_weights:
            break
    return time
            