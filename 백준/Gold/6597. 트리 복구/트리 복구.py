import sys


def postorder(start, end):
    global pre_index
    if start > end:
        return

    mid=inorder.index(preorder[pre_index])
    pre_index+=1
    postorder(start,mid-1)
    postorder(mid+1,end)
    print(inorder[mid],end='')


while True:
    try:
        preorder, inorder = sys.stdin.readline().split()
        pre_index=0
        postorder(0, len(preorder) - 1)
        print()

    except:
        break
