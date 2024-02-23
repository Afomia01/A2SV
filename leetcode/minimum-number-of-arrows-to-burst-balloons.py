class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        start=points[0]
        count=1
        for left, right in points[1:]:
            if left>start[1]:
                count+=1
                start=[1,right]
            else:
                start[1]=min(start[1],right)
        return count
        