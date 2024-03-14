class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift= [0 for i in range(len(s)+1)]
        for start, end ,direction in shifts:
            if direction == 1:
                shift[start]+=1
                shift[end+1]-=1
            elif direction==0:
                shift[start]-=1
                shift[end+1]+=1
        sum=0
        res=[]
        ans=""
        for i in range(len(shift)):
            sum+=shift[i]
            res.append(sum)
        for i in range(len(s)):
            ans+=chr((res[i]+ ord(s[i]) -97)% 26 + 97)
        return ans






        
        