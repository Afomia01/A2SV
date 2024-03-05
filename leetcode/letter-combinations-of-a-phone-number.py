class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        myDict = {
            '2': ['a','b','c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def backtrack(i, cStr):
            if len(cStr)>=len(digits):
                ans.append("".join(cStr))
                return
            for k in myDict[digits[i]]:
                cStr.append(k)
                backtrack(i+1, cStr)
                cStr.pop()
        ans = []
        cStr= []
        if digits=="":
            return []
        backtrack(0,[])
        return ans








            






















