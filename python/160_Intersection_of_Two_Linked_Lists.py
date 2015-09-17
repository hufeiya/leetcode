# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        lengthA,lengthB = 1,1
        tempA,tempB = headA,headB
        while tempA.next:
            lengthA += 1
            tempA = tempA.next
        while tempB.next:
            lengthB += 1
            tempB = tempB.next
        if tempA != tempB:
            return None
        if lengthB > lengthA:
            headA,headB = headB,headA
        for i in xrange(abs(lengthA - lengthB)):
            headA = headA.next
        for i in xrange(lengthB):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
