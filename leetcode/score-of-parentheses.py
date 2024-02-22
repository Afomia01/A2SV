class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        count=0
        for i in s:
            if i=='(':
                stack.append(i)
            else:
                num=0
                while stack[-1]!='(':
                    num+=stack.pop()
                    
                if num ==0:
                    num=1
                else:
                    num*=2
                stack.pop()
                stack.append(num)
        return sum(stack)
        




                
        return count