class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / (x * self.myPow(x, -n - 1))
        elif n % 2 == 0:
            res = self.myPow(x, n // 2)
            return res* res
        return x * self.myPow(x, n - 1)
        
        