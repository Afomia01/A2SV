class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dict={}
        count=0
        for i in answers:
            if i==0:
                count+=1
            else:
                if i not in dict or i==dict[i]:
                    dict[i]=0
                    count +=1+i
                else:
                    dict[i]+=1
        return count