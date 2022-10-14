# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return ListNode('')
        size = 0
        tmp = head
        while True:
            try:
                size += 1
                tmp = tmp.next
            except:
                break
        index = ceil(size/2)
        tmp = head
        while tmp and tmp.next:
            index -= 1
            if index == 1:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head