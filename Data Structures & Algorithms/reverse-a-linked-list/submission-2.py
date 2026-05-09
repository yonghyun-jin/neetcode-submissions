# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1 > 2 > 3 > 4
        prev, curr = None, head

        while curr:
            temp = curr.next # save next node before chnage direction
            curr.next = prev
            prev = curr
            curr = temp
        return prev
