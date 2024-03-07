class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def checker(mid):
            j=0
            i=0
            while i< (len(houses)):
                if abs(houses[i]- heaters[j])> mid:
                    
                    while j <len(heaters) and abs(houses[i]- heaters[j])> mid:
                        j+=1
                    if j==len(heaters):
                        break
                i+=1
            if i==len(houses):
                return True

            return False
        x= max(houses)
        y= max(heaters)
        low= 0
        high= max(x,y)
       
    
        while low<=high:
            mid= (low+ high)//2
            if checker(mid):
                high= mid-1
            else:
                low= mid+1
        return low