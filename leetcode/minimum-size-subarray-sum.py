class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total=0
        ans=float("inf")
        n=len(nums)
        for r in range(n):
            total+=nums[r]
            while total>=target:
                ans=min(r-l+1,ans)
                total-=nums[l]
                l+=1

        return 0 if ans==float("inf") else ans        