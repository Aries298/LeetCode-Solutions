# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        next_node, ans = None, None
        for num in vals:
            ans = ListNode(num, next_node)
            next_node = ans
        return ans if ans else None
                