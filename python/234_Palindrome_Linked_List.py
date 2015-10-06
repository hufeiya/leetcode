# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        listlen = 0
        temp = head
        while temp:
            listlen += 1
            temp = temp.next
        halflen = listlen / 2
        pre = None
        while halflen:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
            halflen -= 1
        if listlen % 2:
            head = head.next
        for i in xrange(listlen / 2):
            if pre.val != head.val:
                return False
            pre,head = pre.next,head.next
        return True
