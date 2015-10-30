class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        width,height = len(matrix[0]),len(matrix)
        for i in xrange(height):
            foundzero = False
            for j in xrange(width):
                if matrix[i][j] == 0:
                    foundzero = True
                    matrix[i][j] = float("inf")
            if not foundzero:
                continue
            for j in xrange(width):
                if matrix[i][j] != float("inf"):
                    matrix[i][j] = 0
        for i in xrange(width):
            foundtarget = False
            for j in xrange(height):
                if matrix[j][i] == float("inf"):
                    foundtarget = True
                    break
            if not foundtarget:
                continue
            for j in xrange(height):
                matrix[j][i] = 0
                
