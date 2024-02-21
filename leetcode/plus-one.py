class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value=0
        for x in digits:
            value= value*10+ x

        value=value+1
        
        digits=[]
        while value>0:
            digits.insert(0,value%10)
            value//=10
        return digits
          
        