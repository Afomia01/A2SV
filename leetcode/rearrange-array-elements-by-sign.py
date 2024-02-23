class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        answer=[0]*len(nums)
        positive=0
        negative=1
        for n in nums:
            if n>0:
                answer[positive]=n
                positive+=2
            elif n<0:
                answer[negative]=n
                negative+=2
        return answer

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        