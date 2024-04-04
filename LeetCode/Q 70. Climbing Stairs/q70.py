class Solution(object):

    def climb(self, n, dp):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if dp[n] != None:
            return dp[n]
        sp1 = self.climb(n - 1, dp)
        sp2 = self.climb(n - 2, dp)
        dp[n] = sp1 + sp2
        return sp1 + sp2

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [None] * (n + 1)
        return self.climb(n, dp)
