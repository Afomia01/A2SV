class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dict= defaultdict(int)
        count=0
        total=0
        dict[0]=1
        for n in nums:
            total+=n
            if total-goal in dict.keys():
                count+=dict[total-goal]
            
            dict[total] += 1
        return count
