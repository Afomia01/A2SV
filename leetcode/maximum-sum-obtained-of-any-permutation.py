class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD= 10**9 +7
        line= [0]*(len(nums)+1)
        for start, end in requests:
            line[start]+=1
            line[end+1]-=1
        sum=0
        prefix=[]
        for i in range(len(line)):
            sum+= line[i]
            prefix.append(sum)
        ans=0
        prefix= sorted(prefix, reverse= True)
        nums= sorted(nums, reverse=True)
        for i in range(len(nums)):
            ans+= prefix[i]*nums[i]
        return ans%MOD

