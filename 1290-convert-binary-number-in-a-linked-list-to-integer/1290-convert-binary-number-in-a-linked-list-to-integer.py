# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num, ans = [], 0
        while head:
            num.append(head.val)
            head = head.next
        return int(''.join([str(n) for n in list((num))]),2)
