import sys

def my_pow(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base

    half = my_pow(base, exp // 2)
    return half * half % MOD if exp % 2 == 0 else half * half * base % MOD

MOD = 1000000007
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
answer = 0

for i in range(N):
    answer += numbers[i] * (my_pow(2, i) - my_pow(2, N - i - 1))
print(answer%MOD)
