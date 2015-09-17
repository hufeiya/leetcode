# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        b = True
        newHead = head
        pre = ListNode(float('inf'))
        while head:
            if head.val == val:
                if b:
                    newHead = head.next
                else:
                    pre.next = head.next
            else:
                b = False
                pre = head
            head = head.next
        return newHead
            
