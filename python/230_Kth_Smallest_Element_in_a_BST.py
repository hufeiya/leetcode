# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.isFound = False
        self.inorder(root)
        return self.result
        
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        if self.isFound:
            return
        if self.k == 1:
            self.result = node.val
            self.isFound = True
            return
        else:
            self.k -= 1
        self.inorder(node.right)

#Another Solution
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        s,itr,count = [],root,0
        while s or itr:
            if itr:
                s.append(itr)
                itr = itr.left
            else:
                itr = s.pop()
                count += 1
                if count == k:return itr.val
                itr = itr.right
