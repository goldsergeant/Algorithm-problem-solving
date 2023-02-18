n = int(input())
prime_numbers = []
answer = 0
a = [False, False]+ [True for i in range(n+1)]

for i in range(2, n + 1):
    if a[i]:
        prime_numbers.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

total=0
end=0
for i in range(len(prime_numbers)):
    while total<n and end<len(prime_numbers):
        total+=prime_numbers[end]
        end+=1
    if total==n:
        answer+=1
    total-=prime_numbers[i]

print(answer)
