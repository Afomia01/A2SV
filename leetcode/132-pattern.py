class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        rightBest=-inf
        for n in range(len(nums)-1,-1,-1):
            if nums[n] <rightBest:
                return True
            while stack and stack[-1]<nums[n] :
                x= stack.pop()
                rightBest=max(x,rightBest)






        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        stack = []
        Min= nums[0]
        for n in nums[1:]:
            while stack and n>=stack[-1][0]:
                stack.pop()
            if stack  and n>stack[-1][1]:
                return True
            stack.append([n, Min])
            Min = min(Min,n)
        return False












        for i, val in enumerate(nums):
            while stack and stack[-1][1] <val:
                stack.pop()
            if stack and stack[-1][1]==val:
                continue
            stack.append((i, val))
        maxi = stack[0][0]
        if len(stack) < 2:
            return False
        else:
            for i in range(maxi):
                if nums[i] < stack[0][1] and nums[i] < stack[1][1]:
                    return True
        return False