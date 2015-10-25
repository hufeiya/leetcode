# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return []
        dummy = ListNode(None)
        dummy.next = head
        result = dummy
        while head and head.next:
            dummy.next = head.next
            temp = head.next
            head.next = temp.next
            temp.next = head
            dummy,head = dummy.next.next,head.next
        return result.next
        
