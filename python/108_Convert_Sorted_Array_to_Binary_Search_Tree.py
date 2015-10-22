# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = nums
        return self.recu(0,len(nums))
        
    def recu(self,left,right):
        if left == right:
            return None
        mid = (left + right)/2
        node = TreeNode(self.nums[mid])
        node.left = self.recu(left,mid)
        node.right =  self.recu(mid + 1,right)
        return node
                
