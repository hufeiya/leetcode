# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == 1:
            return self.reverseList(head,n-m+1)
        else:
            temp = head
            pre = temp
            for i in range(m-1):
                pre = temp
                temp = temp.next
            pre.next = self.reverseList(temp,n-m+1)
            return head
        
    def reverseList(self, head,size):
        dummy = ListNode(float("-inf"))
        tail = head
        save = None
        while head and size:
            save = head.next
            dummy.next, head.next, head = head, dummy.next, head.next
            size -= 1
        if tail:tail.next = save
        return dummy.next
