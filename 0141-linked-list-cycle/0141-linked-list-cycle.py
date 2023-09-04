# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # Initialize two node slow and fast point to the hesd node...
        fastptr = head
        slowptr = head
        while fastptr is not None and fastptr.next is not None:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            if slowptr == fastptr:
                return 1
        return 0