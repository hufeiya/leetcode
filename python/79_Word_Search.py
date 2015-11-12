class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.word = word
        self.result = False
        self.length = len(word)
        self.width = len(board[0])
        self.height = len(board)
        self.board = board;
        self.zeroMatrix = [[False]*self.width for i in xrange(self.height)]
        for i in xrange(self.height):
            for j in xrange(self.width):
                self.dfs(i,j,0)
        return self.result
        
    def dfs(self,i,j,index):
        if self.result or self.zeroMatrix[i][j] == 1 or self.word[index] != self.board[i][j] :
            return
        if index == self.length - 1:
            self.result = True
            return
        self.zeroMatrix[i][j] = True
        if j != 0 and self.zeroMatrix[i][j-1] == False:self.dfs(i,j-1,index+1)
        if j+1 != self.width and self.zeroMatrix[i][j+1] == False:self.dfs(i,j+1,index+1)
        if i != 0 and self.zeroMatrix[i-1][j] == False:self.dfs(i-1,j,index+1)
        if i+1 != self.height and self.zeroMatrix[i+1][j] == False: self.dfs(i+1,j,index+1)
        self.zeroMatrix[i][j] = False
