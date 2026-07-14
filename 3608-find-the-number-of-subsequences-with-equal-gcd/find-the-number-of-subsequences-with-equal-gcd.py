class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        memo = {}

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def dp(i, g1, g2):
            key = (i, g1, g2)
            if key in memo:
                return memo[key]

            if i == n:
                return 1 if g1 != 0 and g1 == g2 else 0

            x = nums[i]

            ans = dp(i + 1, g1, g2)

            ng1 = x if g1 == 0 else gcd(g1, x)
            ans += dp(i + 1, ng1, g2)

            ng2 = x if g2 == 0 else gcd(g2, x)
            ans += dp(i + 1, g1, ng2)

            memo[key] = ans % MOD
            return memo[key]

        return dp(0, 0, 0)