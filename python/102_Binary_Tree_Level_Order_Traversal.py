# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.currentDepth = -1
        self.result = []
        self.dlr(root)
        return self.result
    
    def dlr(self,node):
        if node == None:
            return
        self.currentDepth += 1
        if len(self.result) > self.currentDepth:
            self.result[self.currentDepth].append(node.val)
        else:
            temp = [node.val]
            self.result.append(temp)
        self.dlr(node.left)
        self.dlr(node.right)
        self.currentDepth -= 1
        
