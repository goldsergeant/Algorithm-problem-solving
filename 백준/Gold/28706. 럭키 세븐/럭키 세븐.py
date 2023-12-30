import sys

T = int(sys.stdin.readline())


def compute(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '*':
        return num1 * num2


for _ in range(T):
    K = 1
    N = int(sys.stdin.readline())
    dp = [[False for _ in range(7)] for _ in range(N + 1)]
    dp[0][1] = True

    for i in range(1, N + 1):
        op1, num1, op2, num2 = sys.stdin.readline().split()
        num1=int(num1)
        num2=int(num2)
        for j in range(7):
            if dp[i-1][j]:
                dp[i][compute(j,op1,num1)%7]=True
                dp[i][compute(j,op2,num2)%7]=True

    print('LUCKY' if dp[-1][0] else 'UNLUCKY')