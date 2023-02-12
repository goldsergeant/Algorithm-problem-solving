import collections

t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    deq_s = input()
    deque = collections.deque(map(int, deq_s.strip('[').strip(']').split(','))) if n > 0 else collections.deque()
    flag = 0
    pointer = 0
    for order in p:
        if order == 'R':
            pointer = len(deque) - 1 if pointer == 0 else 0
        elif order == 'D':
            if len(deque) == 0:
                flag = 1
                break
            else:
                deque.popleft() if pointer == 0 else deque.pop()
    if flag == 0:
        if pointer == 0:
            print('[' + ','.join(map(str, deque)) + ']')
        else:
            deque.reverse()
            print('[' + ','.join(map(str, deque)) + ']')
    else:
        print('error')
