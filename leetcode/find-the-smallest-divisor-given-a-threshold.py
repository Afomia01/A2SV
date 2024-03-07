class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def checker(threshold,mid):
            sum=0
            for i in range(len(nums)):
                sum+= ceil(nums[i]/mid)
            if sum >threshold:
                return False
            return True
    
        low= 1
        high= max(nums)
        while low<= high:
            mid= (low+high)//2
            if checker(threshold,mid):
                high= mid-1
            else:
                low= mid+1
        return low
            
            