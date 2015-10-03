# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        self.sublist = []
        self.result = []
        self.order(root)
        return self.result
        
    def order(self,node):
        self.sublist.append(node.val)
        if node.left == None and node.right == None:
            s = ""
            for i in self.sublist:
                s += str(i) + "->"
            if len(s):
                s = s[:-2]
            self.result.append(s)
            self.sublist.pop()
        else:
            if node.left:self.order(node.left)
            if node.right:self.order(node.right)
            self.sublist.pop()
