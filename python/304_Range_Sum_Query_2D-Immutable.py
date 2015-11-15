class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        height,width = len(matrix),len(matrix[0])
        sum = [[0]*(width+1) for i in xrange(height+1)]
        sum[1][1] = matrix[0][0]
        for i in xrange(1,height+1):
            for j in xrange(1,width+1):
                sum[i][j] = sum[i-1][j] + sum [i][j-1] + matrix[i-1][j-1] - sum[i-1][j-1]
        self.sum = sum

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sum[row2+1][col2+1] - self.sum[row1][col2+1] - self.sum[row2+1][col1] + self.sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
