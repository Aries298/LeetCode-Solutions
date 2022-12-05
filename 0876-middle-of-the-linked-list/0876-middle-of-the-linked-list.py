# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        ans = ans[int(len(ans)//2):]
        ans = list(reversed(ans))
        new_node = ListNode(val=ans[0])
        for i in range(1,len(ans)):
            new_node = ListNode(val=ans[i], next=new_node)
        return new_node
            