n = int(input())
prime_numbers = []
answer = 0
a = [False, False]+ [True for i in range(n+1)]

for i in range(2, n + 1):
    if a[i]:
        prime_numbers.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

for i in range(len(prime_numbers)):
    total = n
    for j in range(i, len(prime_numbers)):
        total = sum(prime_numbers[i:j + 1])
        if total == n:
            answer += 1
            break
        elif total > n:
            break

print(answer)
