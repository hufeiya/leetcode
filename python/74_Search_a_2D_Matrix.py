class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m,n = len(matrix),len(matrix[0])
        left,right = 0,m*n
        while left < right:
            mid = (left + right)/2
            if target == matrix[mid/n][mid%n]:
                return True
            elif target < matrix[mid/n][mid%n]:
                right = mid
            else:
                left =  mid + 1
        return False
