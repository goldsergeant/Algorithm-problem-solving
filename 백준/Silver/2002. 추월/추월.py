import collections

N=int(input())
enter_cars=collections.deque()
answer=0
for _ in range(N):
    enter_cars.append(input())

for _ in range(N):
    out_car=input()
    if out_car!=enter_cars[0]:
        answer+=1
        enter_cars.remove(out_car)
    else:
        enter_cars.popleft()

print(answer)

