class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro= prod(nums)
        print(pro)
        ans=[]
        zero_count=0
        for n in nums:
            if n==0:
                zero_count+=1
        if zero_count>1:
            return [0]*len(nums)
        else:
            for i in range(len(nums)):
                if nums[i]!=0:
                    ans.append(pro//nums[i])
                else:
                    x= prod(nums[:i]) * prod(nums[i+1:])
                    ans.append(x)
        return ans
    

    