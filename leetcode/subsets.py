class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i):
            if i>=len(nums):
                ans.append(path[:])
                return
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            backtrack(i+1)
        ans=[]
        path=[]
        backtrack(0)
        return ans




































