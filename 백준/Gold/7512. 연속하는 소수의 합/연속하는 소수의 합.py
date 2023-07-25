import collections

t = int(input())
prime_numbers = []
max_num = 10000001
is_prime = [False, False] + [True] * (max_num - 1)
for i in range(2, max_num):
    if is_prime[i]:
        prime_numbers.append(i)
        for j in range(2 * i, max_num, i):
            is_prime[j] = False

for test_case in range(1, t + 1):
    m = int(input())
    n = list(map(int, input().split()))
    n.sort(reverse=True)

    sum_prime=[[sum(prime_numbers[:n[i]]),0] for i in range(m)]

    while True:
        if is_prime[sum_prime[0][0]]:
            break

        sum_prime[0][0]-=prime_numbers[sum_prime[0][1]]
        sum_prime[0][1]+=1
        sum_prime[0][0]+=prime_numbers[sum_prime[0][1]+n[0]-1]

    index=1

    while True:
        if index==m:
            break

        if index==0:
            while True:
                sum_prime[0][0] -= prime_numbers[sum_prime[0][1]]
                sum_prime[0][1] += 1
                sum_prime[0][0] += prime_numbers[sum_prime[0][1] + n[0] - 1]
                if is_prime[sum_prime[0][0]]:
                    break
            index+=1

        elif sum_prime[index][0]==sum_prime[0][0]:
            index+=1

        elif sum_prime[index][0]>sum_prime[0][0]:
            index=0

        elif sum_prime[index][0]<sum_prime[0][0]:
            sum_prime[index][0]-=prime_numbers[sum_prime[index][1]]
            sum_prime[index][1]+=1
            sum_prime[index][0]+=prime_numbers[sum_prime[index][1]+n[index]-1]

    print(f'Scenario {test_case}:')
    print(sum_prime[0][0])
    print()