class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width,height = len(grid[0]),len(grid)
        minvals = grid[0][:]
        for i in xrange(1,width):
            minvals[i] += minvals[i-1]
        for i in xrange(1,height):
            minvals[0] += grid[i][0]
            for j in xrange(1,width):
                minvals[j] = min(minvals[j] , minvals[j-1]) + grid[i][j]
        return minvals[width-1]
