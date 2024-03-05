class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx):
            if idx== len(nums):
                ans.append(nums[:])
                return 
            
            for i in range(idx, len(nums)):
                nums[idx], nums[i]= nums[i], nums[idx]
                backtrack(idx+1)
                nums[i], nums[idx]= nums[idx], nums[i]   
        ans=[]       
        backtrack(0)
        return ans
                
