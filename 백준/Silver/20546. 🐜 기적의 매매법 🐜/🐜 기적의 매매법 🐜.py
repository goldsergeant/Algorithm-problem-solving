import sys

money = int(input())
price = list(map(int, sys.stdin.readline().split()))

jun_money = money
sung_money = money
jun_stock = 0
sung_stock = 0
for i in range(14):  # 준현
    if price[i] <= money:
        jun_stock = (money // price[i]) * price[-1]
        jun_money = jun_money % price[i]
        break

for i in range(3, 14):
    if i==13:
        sung_money+=(sung_stock*price[-1])
        continue

    if price[i - 3] > price[i - 2] and price[i - 2] > price[i-1] and price[i] <= sung_money:
        sung_stock += (sung_money // price[i])
        sung_money = sung_money % price[i]

    elif price[i - 3] < price[i - 2] and price[i - 2] < price[i-1] and sung_stock>0:
        sung_money += (sung_stock * price[i])
        sung_stock = 0


if jun_stock+jun_money>sung_money:
    print('BNP')
elif jun_stock+jun_money<sung_money:
    print('TIMING')
else:
    print('SAMESAME')