# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = [root]
        result = []
        while len(stack) != 0:
            result.append(root.val)
            if root.left:
                if root.right:
                    stack.append(root.right)
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = stack.pop()
        return result
                
