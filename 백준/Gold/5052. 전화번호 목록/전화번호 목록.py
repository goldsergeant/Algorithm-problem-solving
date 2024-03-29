import sys

T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    numbers=list(sys.stdin.readline().rstrip() for _ in range(N))
    numbers.sort()
    answer='YES'
    for i in range(1,N):
        if numbers[i-1] in numbers[i][:len(numbers[i-1])]:
            answer='NO'
            break

    print(answer)