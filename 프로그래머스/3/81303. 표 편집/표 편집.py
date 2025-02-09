VAL, PREV, NEXT = 0, 1, 2


class ListNode:
    def __init__(self, val=None, prev=None, next=None, row=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.row = row


def up(cnt):
    global cur
    while cnt > 0:
        cur = cur.prev
        cnt -= 1


def down(cnt):
    global cur
    while cnt > 0:
        cur = cur.next
        cnt -= 1


def delete(recent_delete):
    global cur
    recent_delete.append(cur)
    cur.val = 'X'
    prev = cur.prev
    next = cur.next
    if prev is not None:
        prev.next = next
    if next is not None:
        next.prev = prev

    if next is None:
        cur = prev
    else:
        cur = next


def restore(recent_delete, node_id):
    restore_node = recent_delete.pop()
    restore_node.val = 'O'
    prev = restore_node.prev
    next = restore_node.next
    while prev is not None and prev.val=='X': # 삭제 안된것까지 찾아야 함
        prev = prev.prev
    while next is not None and next.val=='X':
        next = next.next

    if prev is not None:  # 되돌릴 노드가 가장 위쪽에 있지 않을때
        prev.next = restore_node
        restore_node.prev = prev

    if next is not None:
        next.prev = restore_node
        restore_node.next = next


def solution(n, k, cmd):
    global cur
    # linked_list[-1][NEXT] = 0
    recent_delete = []
    answer = []
    head = ListNode(val='O', row=0)
    cur = head
    node_id = [cur]
    for i in range(n - 1):
        node = ListNode(val='O', row=i + 1)
        cur.next = node
        node.prev = cur
        node_id.append(node)
        cur = cur.next

    cur = head
    for _ in range(k):
        cur = cur.next

    for st in cmd:
        st = st.split()
        query = st[0]
        if query == 'U':
            cnt = int(st[1])
            up(cnt)

        elif query == 'D':
            cnt = int(st[1])
            down(cnt)
        elif query == 'C':
            delete(recent_delete)
        elif query == 'Z':
            restore(recent_delete, node_id)
    for i in range(len(node_id)):
        answer.append(node_id[i].val)
    return ''.join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
