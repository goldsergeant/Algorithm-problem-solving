import sys

N, K, P, X = map(int, sys.stdin.readline().split())

numbers = ['1111110', '0110000', '1101101', '1111001', '0110011', '1011011',
       '1011111', '1110000', '1111111', '1111011']
possible_nums=set()
need_cnt = [[0 for _ in range(10)] for _ in range(10)]

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i!=j:
            temp = 0
            for k in range(7):
                if numbers[i][k] != numbers[j][k]:
                    temp += 1

            need_cnt[i][j] = temp


def dfs(led_num, depth, reverse_cnt):
    global answer
    if depth == K:
        if 1<=int(led_num)<=N and int(led_num)!=X:
            possible_nums.add(int(led_num))
        return

    for i in range(10):
        target=led_num[depth]
        if reverse_cnt+need_cnt[int(target)][i]<=P:
            new_led_num=led_num[:depth]+str(i)+led_num[depth+1:]
            dfs(new_led_num,depth+1,reverse_cnt+need_cnt[int(target)][i])

    dfs(led_num,depth+1,reverse_cnt)
led_x = str(X).zfill(K)
dfs(led_x,0,0)
print(len(possible_nums))
