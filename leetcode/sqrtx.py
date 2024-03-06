class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1 or x==0:
            return x
        low= 1
        high= x
        while low<= high:
            mid=(low+ high)//2
            if mid*mid >x:
                high= mid-1
            elif mid*mid <x:
                low= mid+1
            else:
                return mid
        return (high)