import sys

def print_st():
    cnt=0
    for i in range(len(string)):
        if visited[i]:
            print(string[i],end='')
            cnt+=1
    if cnt<len(string):
        print()
def make_string(left, right):
    global st
    # print(left,right)
    if left>right:
        return
    idx = left
    ch='Z'
    for i in range(left,right+1):
        if string[i]<ch:
            ch=string[i]
            idx=i

    visited[idx]=True
    print_st()
    make_string(idx + 1, right)
    make_string(left, idx - 1)


string = sys.stdin.readline().rstrip()
visited=[False for _ in range(len(string))]
make_string(0, len(string) - 1)