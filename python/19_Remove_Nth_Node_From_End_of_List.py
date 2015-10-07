# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre,target,temp = None,head,head
        while n:
            temp = temp.next
            n -= 1
        while temp:
            temp,pre,target = temp.next,target,target.next
        if not pre:
            return target.next
        else:
            pre.next = target.next
            return head
