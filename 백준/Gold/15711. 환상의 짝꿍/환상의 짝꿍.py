import sys

t = int(sys.stdin.readline())
max_num = 2000000
is_prime = [True] * (max_num + 1)
is_prime[0]=is_prime[1]=False
for i in range(2, max_num + 1):
    if is_prime[i]:
        for j in range(2 * i, max_num + 1, i):
            is_prime[j] = False

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    total = a + b
    if total % 2 == 0:  # 짝수일때
        if total > 2:
            print('YES')
        else:
            print('NO')
    else:  # 홀수일때
        if total <= max_num:
            if is_prime[total - 2]:
                print('YES')
            else:
                print('NO')
        else:
            flag = False
            for i in range(2, max_num + 1):
                if is_prime[i] and (total - 2) % i == 0:
                    print('NO')
                    flag = True
                    break
            if not flag:
                print('YES')
