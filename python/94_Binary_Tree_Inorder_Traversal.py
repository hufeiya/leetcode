# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        stack = []
        while root != None or len(stack) != 0:
            while root != None:
                stack.append(root)
                root = root.left
            if len(stack) != 0:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result
                
