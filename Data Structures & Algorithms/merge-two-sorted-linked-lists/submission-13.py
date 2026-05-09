# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Goal : Merge two linkedlist in sort manner

        dummy = head = ListNode()


        while list1 and list2:
        # compare list1 val and list2 val
        # update list1 and list 2 if it is merged to the head
        # attach list1 and 2 to the head node.
            if list1.val > list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
        # move head node so that we can attach node everytime
            head = head.next
        if list1:
            head.next = list1
        if list2:
            head.next = list2
        
        return dummy.next