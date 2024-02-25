class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum1 = 0
        sum2= 0
        
        for i in range(n):
            sum1+= mat[i][i]  
            sum2 += mat[i][n - i - 1]  
            
        if n % 2 == 1:
            return sum1+ sum2 - mat[n // 2][n // 2]
        else:
            return sum1 + sum2

        