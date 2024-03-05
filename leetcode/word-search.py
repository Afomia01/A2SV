class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row= len(board)
        col= len(board[0])
        dir = [(1,0), (-1,0), (0,1), (0,-1)]
        flag= set()
        def inbound(r, c):
            if r<row and r>=0 and c<col and c>=0:
                return True

        def backtrack(i,j,k):
            if k== len(word):
                return True
            
            for x,y in dir:
                if (i+x, j+y) not in flag and inbound(i+x, j+y) and board[i+x][j+y]==word[k]:
                    flag.add((i+x, j+y))
                    res = backtrack(i+x, j+y, k+1)
                    if res:
                        return True
                    flag.remove((i+x, j+y))
                
                    
                  
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    flag.add((i,j))
                    ans= backtrack(i,j,1)
                    if ans:
                        return True
                    flag.remove((i,j))
        



        