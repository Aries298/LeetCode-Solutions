# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        vals1 = []
        vals2 = []
        while list1:
            vals1.append(list1.val)
            list1 = list1.next
        while list2:
            vals2.append(list2.val)
            list2 = list2.next
            
        sorted_list = sorted(vals1+vals2)
        
        ans = None
        for num in sorted_list:
            tmp = ListNode(num)
            if (ans == None):
                ans = tmp
            else:
                ptr = ans
                while (ptr.next != None):
                    ptr = ptr.next
                ptr.next = tmp
                
        return ans