class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = dict()
        def dp(i):
            if i < 0:
                return 0
            if not i in memo:
                memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            return memo[i]
        return dp(len(nums)-1)

