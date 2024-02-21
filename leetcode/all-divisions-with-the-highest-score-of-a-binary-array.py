class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right= sum(nums)
        
        score = [left+right]
      
        
        for i in range(n):
            if nums[i] == 0:
                left += 1
            else:
                right -= 1
            
            score.append(left+right)
        maxi= max(score)
        return ([ i for i, x in enumerate(score) if x==maxi])