class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:-abs(x[0]-x[1]))
        print(costs)
        countA=0
        countB=0
        n= len(costs)
        sumA=0
        sumB=0
        for i in range(n):
            minimum=min(costs[i][0], costs[i][1])
            if (countA<n/2 and minimum==costs[i][0]):
                countA+=1
                sumA+= minimum
            elif (countB<n/2 and minimum==costs[i][1]):
                countB+=1
                sumB+= minimum
            elif countB>=n/2:
                countA+=1
                sumA+= costs[i][0]
            elif countA>=n/2:
                countB+=1
                sumB+= costs[i][1]
        return sumA+sumB
        




         