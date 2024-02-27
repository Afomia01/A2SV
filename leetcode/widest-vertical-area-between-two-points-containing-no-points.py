class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        xArr=[]
        maxx=0

        for i in range(len(points)):
            xArr.append(points[i][0])
        for i in range(len(xArr)-1):
            diff= xArr[i+1]-xArr[i]
            maxx= max(diff, maxx)
        return maxx




        