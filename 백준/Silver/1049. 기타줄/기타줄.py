import sys

N,M=map(int,sys.stdin.readline().split())
answer=sys.maxsize
packages=[]
each_arr=[]
for _ in range(M):
    package,each=map(int,sys.stdin.readline().split())
    packages.append(package)
    each_arr.append(each)


min_package=min(packages)
min_each=min(each_arr)
if min_package<min_each*6:
    if min_package<(N%6)*min_each:
        answer=min(answer,(N//6)*min_package+min_package)
    else:
        answer=min(answer,(N//6)*min_package+(min_each*(N%6)))
else:
    answer=min(answer,N*min_each)

print(answer)