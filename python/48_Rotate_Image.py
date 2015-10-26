class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        halflen = length / 2
        for i in xrange(1,length):
            for j in xrange(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in xrange(length):
            for j in xrange(halflen):
                matrix[i][j],matrix[i][length-j-1] = matrix[i][length-j-1],matrix[i][j]
