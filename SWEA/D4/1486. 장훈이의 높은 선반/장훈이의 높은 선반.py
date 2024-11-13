import itertools

T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    top_heights = []

    for cnt in range(1, N + 1):
        for case in itertools.combinations(heights, cnt):
            top_heights.append(sum(case))

    target=sorted(filter(lambda x:x>=B, top_heights))[0]
    print(f'#{test_case} {target-B}')
