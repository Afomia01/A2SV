class NumArray:

    def __init__(self, nums: List[int]):
        self.nums= nums
        sum=0
        self.running=[0]
        for i in range(len(nums)):
            sum+=nums[i]
            self.running.append(sum)
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.running[right+1]- self.running[left]

        

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)