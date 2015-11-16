# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:return
        dummy = ListNode(0)
        dummy.next = head
        duplicate = head.val
        node = dummy
        while node.next:
            if node.next.next and node.next.val == node.next.next.val:
                duplicate = node.next.val
                temp = node.next
                while temp and temp.val == duplicate:
                    temp = temp.next
                node.next = temp
            else:
                node = node.next
        return dummy.next
