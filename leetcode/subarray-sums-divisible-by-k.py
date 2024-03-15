class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        box= defaultdict(int)
        count=0
        total=0
        box[0]=1
        for n in nums:
            total+=n
            modi= total%k
            if modi in  box.keys():
                count+=box[modi]
            box[modi]+=1
        return count