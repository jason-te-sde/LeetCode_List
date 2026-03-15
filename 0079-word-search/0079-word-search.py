class Solution:
    def __init__(self):
        self.found = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, word, 0)
                if self.found:
                    return True
        return False
    
    def dfs(self, board, i, j, word, p):
        if p == len(word):
            self.found = True
            return
        if self.found:
            return
        
        m, n = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return
        if board[i][j] != word[p]:
            return
        
        temp = board[i][j]
        board[i][j] = '#'
        self.dfs(board, i + 1, j, word, p + 1)
        self.dfs(board, i , j + 1, word, p + 1)
        self.dfs(board, i - 1, j, word, p + 1)
        self.dfs(board, i, j - 1, word, p + 1)
        board[i][j] = temp

        