class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count=0
        count=0
        vowels='aeiou'

        for i, c in enumerate(s):
            if c in vowels:
                count+=1
            if i>=k and s[i-k] in vowels:
                count-=1
            max_count= max(count, max_count)
        
        return max_count

