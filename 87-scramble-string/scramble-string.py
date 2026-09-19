class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        from functools import lru_cache

        @lru_cache(None)
        def dp(a, b):
            # Same string
            if a == b:
                return True

            # Different characters -> impossible
            if sorted(a) != sorted(b):
                return False

            n = len(a)

            # Try every possible split
            for i in range(1, n):

                # Case 1: No swap
                if dp(a[:i], b[:i]) and dp(a[i:], b[i:]):
                    return True

                # Case 2: Swap
                if dp(a[:i], b[n-i:]) and dp(a[i:], b[:n-i]):
                    return True

            return False

        return dp(s1, s2)