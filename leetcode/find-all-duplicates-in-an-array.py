class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            idx= abs(nums[i])-1
            if nums[idx]<0:
                ans.append(idx+1)
            nums[idx]= -(nums[idx])
        return ans


        
        
        # i=0
        # ans=[]
        # count=0
        # while i<len(nums):
        #     x= nums[i]-1
        #     if x==i:
        #         count+=1
        #         if count==2:
        #             ans.append(i)
        #         i+=1
        #     else:
        #         nums[x], nums[i]= nums[x], nums[i]
                
                
        # return ans

        