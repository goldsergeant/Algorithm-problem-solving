# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root=node=ListNode(0)
        node.next=head
        while head and head.next:
            prev=head
            head=head.next
            node.next=head
            prev.next=head.next
            head.next=prev
            head=prev.next
            node=prev
        return root.next