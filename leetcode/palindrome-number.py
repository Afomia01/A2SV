class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            new= str(x)
            new= new[::-1]
            if x== int(new):
                return True
            else:
                return False
        