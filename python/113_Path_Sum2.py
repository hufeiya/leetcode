# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        self.result = 0
        self.retList = []
        self.tempList = []
        self.target = sum
        self.digui(root)
        return self.retList
        
    def digui(self,node):
        if node == None:
            return
        self.tempList.append(node.val)
        self.result += node.val
        self.digui(node.left)
        self.digui(node.right)
        if node.left == None and node.right == None and self.result == self.target:
            self.retList.append(self.tempList[:])
        self.tempList.pop()
        self.result -= node.val   
