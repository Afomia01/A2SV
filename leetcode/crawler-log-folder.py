class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]

        for i in logs:
            if i.startswith('../'):
                if stack:
                    stack.pop()
            elif i.startswith('./'):
                continue
            else:
                stack.append(i)
        return len(stack)

        