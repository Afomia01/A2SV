class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, h = 0, len(s) - 1
        s = s.lower()
        while l <= h:
            if not s[l].isalnum():
                l += 1
            elif not s[h].isalnum():
                h -= 1
            elif s[l] != s[h]:
                return False
            else:
                l += 1
                h -= 1
        return True

        