# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        
        cur, len = head, 1
        while cur.next:
            cur = cur.next
            len += 1
        cur.next = head
        
        cur = head
        shift = len - k%len - 1 
        while shift > 0:
            cur = cur.next
            shift -= 1
        
        result = cur.next
        cur.next = None
        
        return result
        
