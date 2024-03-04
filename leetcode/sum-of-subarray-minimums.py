class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        MOD=10**9 +7
        length = len(nums)
        left = [-1] * length
        right = [length] * length
        stk = []

        for i in range(length):
            while stk and nums[stk[-1]] >= nums[i]:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)

        stk = []

        for i in range(length - 1, -1, -1):
            while stk and nums[stk[-1]] > nums[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)

        total_sum = 0

        for i in range(length):
            total_sum += (i - left[i]) * (right[i] - i) * nums[i] % MOD
            total_sum %= MOD

        return total_sum
        