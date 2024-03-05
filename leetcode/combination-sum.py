class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(j, comb):
            if sum(comb)==target:
                new=sorted(comb)
                ans.add(tuple(new))
                return 
            for i in range(len(candidates)):
                if sum(comb)>target:
                    return
                comb.append(candidates[i])
                backtracking(i+1,comb)
                comb.pop()
            
        total=0
        ans=set()
        backtracking(0,[])
        return list(ans)




            

        