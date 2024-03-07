class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        myDict= defaultdict(int)
        
        first=[]
        second=[]
        ans=[]
        for i in range(len(intervals)):
            first.append(intervals[i][0])
            second.append(intervals[i][1])
        for i in range(len(first)):
            myDict[first[i]]= i
        first.sort()
        for i in range(len(second)):
            if second[i] not in first and max(first)< second[i]:
                ans.append(-1)
            else:
                idx= bisect_left(first, second[i])
                num= first[idx]
                ans.append(myDict[num])
        return ans








     

            
        