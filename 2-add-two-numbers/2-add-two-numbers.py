# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = b = ""
        while(l1):
            a += str(l1.val)
            l1 = l1.next
        while(l2):
            b += str(l2.val)
            l2 = l2.next
        ans = int(a[::-1]) + int(b[::-1])
        l3 = None
        for num in str(ans):
            tmp = ListNode(num)
            tmp.next = l3
            l3 = tmp
        return l3

 