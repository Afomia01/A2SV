class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Scount= Counter(s)
        Tcount= Counter(t)
        if Scount==Tcount:
            return True
        return False
        