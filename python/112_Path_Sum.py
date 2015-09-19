# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.result = 0
        self.ret = False
        self.target = sum
        self.digui(root)
        return self.ret
        
    def digui(self,node):
        if self.ret or node == None:
            return
        self.result += node.val
        self.digui(node.left)
        self.digui(node.right)
        if node.left == None and node.right == None and self.result == self.target:
            self.ret = True
            return
        self.result -= node.val
