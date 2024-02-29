class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        for i in range(n):
            minimum=i
            for j in range(i,n):
                if nums[minimum]>nums[j]:
                    minimum = j
            nums[i], nums[minimum]= nums[minimum], nums[i]
        