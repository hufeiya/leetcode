# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            head = ListNode(0)
            p = head
            flag = 0
            while l1 and l2:
                p.val = (l1.val + l2.val + flag) % 10
                flag = (l1.val + l2.val + flag) / 10
                p.next = ListNode(0)
                back = p
                p = p.next
                l1 = l1.next
                l2 = l2.next
            if l1:
                while l1:
                    p.val = (l1.val + flag) % 10
                    flag = (l1.val + flag) / 10
                    p.next = ListNode(0)
                    back = p
                    p = p.next
                    l1 = l1.next
            elif l2:
                while l2:
                    p.val = (l2.val + flag) % 10
                    flag = (l2.val + flag) / 10
                    p.next = ListNode(0)
                    back = p
                    p = p.next
                    l2 = l2.next
                    
            if flag == 1:
                p.val = 1
            else:
                del p
                back.next = None
        return head
