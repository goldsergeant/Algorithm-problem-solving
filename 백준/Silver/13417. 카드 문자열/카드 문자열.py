import collections

T=int(input())
for _ in range(T):
    N=int(input())
    arr=list(input().split())
    answer=collections.deque()
    check_num=arr[0]
    for num in arr:
        if num<=check_num:
            answer.appendleft(num)
            check_num=num
        else:
            answer.append(num)

    print(''.join(answer))
