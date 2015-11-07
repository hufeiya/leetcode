# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        node = root
        stack = []
        while node:
            if node.left:
                if node.right:
                    stack.append(node.right)
                node.right = node.left
                node.left = None
            elif node.right is None and len(stack):
                node.right = stack.pop()
            node = node.right
