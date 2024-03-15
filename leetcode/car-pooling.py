class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxD= trips[0][2]
        for i in (trips):
            maxD= max(maxD, i[2])
        line= [0]*(maxD+1)

        for ppl, fromi, toi in trips:
            line[fromi]+=ppl
            line[toi]-=ppl
        prefix=[]
        sum=0
        for i in range(len(line)):
            sum+=line[i]
            if sum >capacity:
                return False
        return True
        





       

            
       

        