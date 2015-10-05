# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:return True
        return self.dfs(root.left,root.right)
        
    def dfs(self,left,right):
        if not (left or right):return True
        elif bool(left) ^ bool(right) or left.val != right.val:return False
        else:return self.dfs(left.left,right.right) and self.dfs(left.right,right.left)
        
