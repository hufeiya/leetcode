# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        self.invert(root)
        return root
        
    def invert(self,node):
        if node != None:
            temp = node.left
            node.left = node.right
            node.right = temp
            self.invert(node.left)
            self.invert(node.right)
