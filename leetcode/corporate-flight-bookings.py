class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        line= [0]*(n+1)
        for start, end , add in bookings:
            line[start-1]+=add
            line[end]-=add
        prefix=[]
        sum=0
        for i in range(len(line)):
            sum+=line[i]
            prefix.append(sum)
        prefix.pop()
       #prefix.remove(prefix[0])
        return prefix
            
        