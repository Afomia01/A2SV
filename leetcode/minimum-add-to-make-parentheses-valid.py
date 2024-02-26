class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        x=0
        y=0
        for i in s:
            if i=='(':
                x+=1
            else:
                if x:
                    x-=1
                else:
                    y+=1
        return x+y
        