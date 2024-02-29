class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sumleft= 0
        sumright= sum(nums)
        for i in range(len(nums)):
            if sumleft == sumright - nums[i]:
                return i
            sumleft+=nums[i]
            sumright -= nums[i]

        return -1
            