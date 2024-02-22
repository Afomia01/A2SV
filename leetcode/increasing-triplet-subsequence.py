class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minval1=float('inf')
        minval2=float('inf')
        for num in nums:
            if num <= minval1:
                minval1 = num
            elif num <= minval2:
                minval2 = num
            else:
                return True

        return False



        