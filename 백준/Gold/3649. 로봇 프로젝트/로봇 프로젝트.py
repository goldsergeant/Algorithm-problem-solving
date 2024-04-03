import sys

while True:
    try:
        x=int(sys.stdin.readline())
        x*=10000000
        flag=False
        n=int(sys.stdin.readline())
        legos=list(int(sys.stdin.readline()) for _ in range(n))
        legos.sort()
        left=0
        right=n-1
        while left<right:
            total=legos[left]+legos[right]
            if total<x:
                left+=1
            elif total>x:
                right-=1
            else:
                print(f'yes {legos[left]} {legos[right]}')
                flag=True
                break

        if not flag:
            print('danger')

    except:
        break