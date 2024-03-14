class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        box= defaultdict(int)
        count=0
        total=0
        box[0]=1
        for n in nums:
            total+=n
            if total-k in box.keys():
                count+=box[total-k]
            box[total]+=1
        return count

        