# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        tmp = ListNode(-1)
        tmp.next = head
        curr_head = tmp
        while curr_head.next:
            if curr_head.next.val == val:
                curr_head.next = curr_head.next.next
            else:
                curr_head = curr_head.next
        return tmp.next