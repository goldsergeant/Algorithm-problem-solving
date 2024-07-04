import sys

while True:
    try:
        N=int(sys.stdin.readline())
        tmp = 1
        while True:
            tmp *= 9
            if tmp >= N:
                print('Baekjoon wins.')
                break

            tmp *= 2
            if tmp >= N:
                print('Donghyuk wins.')
                break
    except:
        break

