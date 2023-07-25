import collections
import heapq

t = int(input())
prime_numbers = []
max_num = 10000001
is_prime = [False, False] + [True] * (max_num - 1)
for i in range(2, max_num):
    if is_prime[i]:
        prime_numbers.append(i)
        for j in range(2 * i, max_num, i):
            is_prime[j] = False

def slide_to_prime(total,start,end):
    total+=prime_numbers[end+1]-prime_numbers[start]
    start+=1
    end+=1
    while not is_prime[total]:
        total += prime_numbers[end + 1] - prime_numbers[start]
        start += 1
        end += 1
    return [total,start,end]

for test_case in range(1, t + 1):
    m = int(input())
    n = list(map(int, input().split()))

    arr=[]
    for element in n:
        total=sum(prime_numbers[:element])
        start=0
        end=element-1
        if is_prime[total]:
            heapq.heappush(arr,[total,start,end])
        else:
            heapq.heappush(arr,slide_to_prime(total,start,end))


    while not all(i[0]==arr[0][0] for i in arr):
        total,start,end=heapq.heappop(arr)
        heapq.heappush(arr,slide_to_prime(total,start,end))


    print(f'Scenario {test_case}:')
    print(arr[0][0])
    print()