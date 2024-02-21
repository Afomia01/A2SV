class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n= len(grid)-2
        m= len(grid[0])-2
        final=0
        for i in range(n):
            for j in range(m):
                sum= grid[i][j]+grid[i][j+1]+ grid[i][j+2]+grid[i+1][j+1]+ grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                final=max(sum,final)
        return final
                
            

        return sum
        