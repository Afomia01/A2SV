class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax=[]
        colMax=[]
        result=0
        for i in range(len(grid)):
            rowMax.append(max(grid[i]))
        for i in range(len(grid)):
            maxx =-1
            for j in range(len(grid[0])):
               maxx=max(grid[j][i], maxx)
            colMax.append(maxx)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += (min(rowMax[i], colMax[j]))-grid[i][j]
        print(rowMax)
        print(colMax)
        return result
        


        