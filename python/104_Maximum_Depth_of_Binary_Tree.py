# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.maxDp = -float('inf')
        self.currentDepth = 0
        self.findMax(root)
        return self.maxDp
        
    def findMax(self,node):
        if node == None:
            return
        self.currentDepth += 1
        if node.left == None and node.right == None:
            self.maxDp = max(self.maxDp,self.currentDepth)
            return
        if node.left:
            self.findMax(node.left)
            self.currentDepth -= 1
        if node.right:
            self.findMax(node.right)
            self.currentDepth -= 1
        
