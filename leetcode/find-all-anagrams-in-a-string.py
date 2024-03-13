class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k= len(p)
        Scount= Counter(s[:k])
        Pcount= Counter(p)
       
        ans=[]
        for i in range(k, len(s)):
            print(Scount)
            if Scount==Pcount:
                ans.append(i-k)
            Scount[s[i-k]]-=1
            if Scount[s[i-k]]==0:
                del Scount[s[i-k]]
            if s[i] in Scount:
                Scount[s[i]]+=1
            else:
                Scount[s[i]]=1
        if Scount==Pcount:
            ans.append(len(s)-k)
            
        return ans



        