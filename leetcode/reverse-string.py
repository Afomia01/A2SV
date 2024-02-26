class Solution:
    def reverse(self, s, start, end):
        if start>=end:
            return 
        s[start],s[end]= s[end],s[start]
        self.reverse(s, start+1,end-1)


    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s,0,len(s)-1)
        