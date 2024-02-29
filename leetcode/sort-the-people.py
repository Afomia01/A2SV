class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people={}
        Originalnames ={}
        for i in range(len(names)):
            if names[i] in people:
                people[names[i] + str(i)]= heights[i]
                Originalnames[names[i]+ str(i)]= names[i]
            else:
                people[names[i]]= heights[i]
                Originalnames[names[i]]= names[i]

        sortheights= dict(sorted(people.items(), key= lambda item: item[-1], reverse=True ))
        final=[]
        for names in sortheights:
            final.append(Originalnames[names])
        return final

       
        