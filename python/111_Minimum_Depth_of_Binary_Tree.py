# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.minDp = float('inf')
        self.currentDepth = 0
        self.findMin(root)
        return self.minDp
        
    def findMin(self,node):
        if node == None:
            return
        self.currentDepth += 1
        if node.left == None and node.right == None:
            self.minDp = min(self.minDp,self.currentDepth)
            return
        if node.left:
            self.findMin(node.left)
            self.currentDepth -= 1
        if node.right:
            self.findMin(node.right)
            self.currentDepth -= 1
        
