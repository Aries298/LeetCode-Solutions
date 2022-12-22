# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        first, second = vals[:int(len(vals)/2)], vals[int(len(vals)/2):][::-1]
        return max([a+b for a,b in zip(first,second)])