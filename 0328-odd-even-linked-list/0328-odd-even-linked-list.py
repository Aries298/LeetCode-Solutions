# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds, evens = [], []
        switch = True
        while head:
            if switch:
                switch = not switch
                odds.append(head.val)
            else:
                switch = not switch
                evens.append(head.val)
            head = head.next
            
        ans = list(reversed(odds+evens))
        if not ans:
            return None
        new_head = ListNode(val=ans[0])
        for i in range(1,len(ans)):
            new_head = ListNode(val=ans[i], next=new_head)
        return new_head
    