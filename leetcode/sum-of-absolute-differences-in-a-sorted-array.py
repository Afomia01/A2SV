class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sumi = sum(nums)
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            nums[i]= (((i+1)*nums[i]-prefix)+(sumi-prefix)-(len(nums)-i-1)*nums[i])
        return nums
        