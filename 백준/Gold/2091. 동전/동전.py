X, A, B, C, D = map(int, input().split())
dp = [(0, 0, 0, 0) for _ in range(X + 1)]

for i in range(1, X+1):
    for cent in (1, 5, 10, 25):
        if i - cent < 0:
            continue
        one,five,ten,twenty_five=dp[i-cent]

        if sum(dp[i])<one+five+ten+twenty_five+1 and one+five*5+ten*10+twenty_five*25==i-cent:
            if cent==1 and one<A:
                dp[i]=(one+1,five,ten,twenty_five)
            elif cent==5 and five<B:
                dp[i] = (one, five+1, ten, twenty_five)
            elif cent==10 and ten<C:
                dp[i] = (one, five, ten+1, twenty_five)
            elif cent==25 and twenty_five<D:
                dp[i] = (one, five, ten, twenty_five+1)


print(*dp[X])
