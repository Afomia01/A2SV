class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter=defaultdict(int)
        ans=0
        for letter in s:
           counter[letter]+=1
        odd = False
        for val in counter.values():
            if val%2==0:
                ans+=val
            else:
                odd=True
                ans+=val-1
        if odd:
            ans+=1

        
            
            
            
        return ans


       
       
       
       
       
       # my_set= set()
        #for letter in s:
            #if letter not in my_set:
               # my_set.add(letter)
            #else:
                #my_set.pop()
        #return len(s)-len(my_set)+1
            
            
        