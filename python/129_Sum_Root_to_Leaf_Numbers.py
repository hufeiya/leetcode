# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.order(root,0)
        
    def order(self,node,sum):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.val + sum*10
        return self.order(node.left,sum*10+node.val)+self.order(node.right,sum*10+node.val)
