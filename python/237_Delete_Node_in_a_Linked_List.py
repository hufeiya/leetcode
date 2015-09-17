# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node and node.next:
            toBeDeleted = node.next
            node.next = toBeDeleted.next
            node.val = toBeDeleted.val
            del toBeDeleted
