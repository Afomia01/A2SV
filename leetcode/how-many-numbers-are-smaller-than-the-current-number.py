class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp= sorted(nums)
        link={}
        ans=[]
        for i in range(len(temp)):
            if temp[i] not in link:
                link[temp[i]]=i
        for i in range(len(nums)):
            ans.append(link[nums[i]])
        return ans
