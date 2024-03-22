class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def Quick(nums,k):
            pivot= random.randint(0, len(nums)-1)
            left, right, mid=[], [] ,[]

            for i in range(len(nums)):
                if nums[i] < nums[pivot]:
                    right.append(nums[i])
                elif nums[i]> nums[pivot]:
                    left.append(nums[i])
                else:
                    mid.append(nums[i])

            if k<= len(left):
                return Quick(left, k)
            if len(left)+ len(mid)<k:
                return Quick(right, k-len(left)-len(mid))
            
            return nums[pivot]

        return Quick(nums,k)

            



        