class Solution:
    def rob(self, nums):
        dp = [None] * (len(nums) + 10)
        return self.robbing(nums, dp)

    def robbing(self, nums, dp):
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]

        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]

        return max(dp[len(nums) - 1], dp[len(nums) - 2])
