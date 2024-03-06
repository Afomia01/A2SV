class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high= len(nums)-1
        ans= [-1,-1]
        while low<=high:
            mid= (low+high)//2
            if target == nums[mid]:
                ans[0]=mid
                high= mid -1
            elif target > nums[mid]:
                low= mid+1
            else:
                high= mid-1
        low=0
        high= len(nums)-1  
        while low<=high:
            mid= (low+high)//2
            if target == nums[mid]:
                ans[1]=mid
                low= mid+1
            elif target < nums[mid]: 
                high= mid -1
            else:
                low= mid+1
        return ans

        





                

        