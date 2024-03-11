class Solution: 
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]: 
         
        def bsl (q): 
            left = 0 
            right = len(candles) - 1 
            while left <= right : 
                mid = (right + left) // 2 
                if candles[mid] < q: 
                    left = mid + 1 
                else: 
                    right = mid - 1 
            if left == len(candles): 
                left -= 1 
             
            return left 
 
        def bsr (q): 
 
            left = 0 
            right = len(candles) - 1 
 
            while left <= right : 
 
                mid = (right + left) // 2 
 
                if candles[mid] <= q: 
                    left = mid + 1 
 
                else: 
                    right = mid - 1 
 
            if right == -1: 
                right += 1 
             
            return right 
 
        arr= [] 
        candles = [] 
 
        for i in range(len(s)): 
 
            if s[i] == "*": 
                arr.append(1) 
            else: 
                arr.append(0) 
                candles.append(i) 
        
         
        if len(candles) == 0: 
            return [0] 
        for i in range(1, len(arr)): 
 
            arr[i] += arr[i-1] 
 
        ans = [0] * len(queries) 
 
 
        for i in range(len(queries)): 
 
            start = candles[bsl(queries[i][0])] 
            end = candles[bsr(queries[i][1])] 
            print(start, end) 
           
            if start <= end: 
             
                ans[i] = arr[end] - arr[start] 
 
        return ans