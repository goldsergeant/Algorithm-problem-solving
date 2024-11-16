VALUE, LEFT, RIGHT = 0, 1, 2

def calc_tree(node):
    if type(tree[node][VALUE]) is int:
        return tree[node][VALUE]

    left=calc_tree(tree[node][LEFT])
    right=calc_tree(tree[node][RIGHT])
    opt=tree[node][VALUE]

    val=0
    if opt=='+':
        val=left+right
    elif opt=='-':
        val=left-right
    elif opt=='*':
        val=left*right
    elif opt=='/':
        val=left//right

    return val

for test_case in range(1, 10 + 1):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N + 1)]
    for _ in range(N):
        arr = list(map(lambda x: int(x) if x.isnumeric() else x, input().split()))
        if type(arr[1]) is int:
            tree[arr[0]][VALUE] = arr[1]
        else:
            tree[arr[0]]= [arr[1],arr[2],arr[3]]

    print(f'#{test_case} {calc_tree(1)}')