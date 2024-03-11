class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
        cSum = maxSum= sum(nums[:k])
        for i in range(k, len(nums)):
            cSum +=nums[i] - nums[i-k]
            maxSum = max(maxSum, cSum)
        
        return maxSum/k