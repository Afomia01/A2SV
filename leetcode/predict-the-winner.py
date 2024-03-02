class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def solve(left, right):
            if left > right:
                return 0, 0
            
            curr1, nxt1 = solve(left+1, right)
            curr2, nxt2 = solve(left, right-1)
                        
            if nums[left] + nxt1 > nums[right] + nxt2:
                return nums[left] + nxt1, curr1
            
            return nums[right] + nxt2, curr2
        
        player1, player2 = solve(0, len(nums)-1)
        
        return player1 >= player2