import sys
from math import sqrt

x, y, d, t = map(int, sys.stdin.readline().split())
distance = sqrt((x ** 2) + (y ** 2))

if distance>=d:
    jump=distance//d
    print(min(distance,(jump+1)*t,(jump*t)+(distance%d)))
else:
    print(min(distance,t+(d-distance),2*t))

