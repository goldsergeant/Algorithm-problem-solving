# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ha=headA
        hb=headB
        lenA=lenB=0
        while ha:
            lenA+=1
            ha=ha.next
        while hb:
            lenB+=1
            hb=hb.next
        if lenA>lenB:
            for i in range(lenA-lenB):
                headA=headA.next
        elif lenA<lenB:
            for i in range(lenB-lenA):
                headB=headB.next
        while headA and headB:
            if headA==headB:
                return headA
            headA,headB=headA.next,headB.next
        return None