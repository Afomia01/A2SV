class Solution:
    def simplifyPath(self, path: str) -> str:
        c= path.split('/')
        stack=[]
        for i in c:
            if i!='.' and i!='..' and i:
                stack.append(i)
            elif i=="..":
                if stack:
                    stack.pop()
        return '/'+ '/'.join(stack)



            


        