class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(start, current):
            # Combination is complete
            if len(current) == k:
                result.append(current.copy())
                return

            # Try every possible next number
            for i in range(start, n + 1):
                current.append(i)

                backtrack(i + 1, current)

                # Backtrack
                current.pop()

        backtrack(1, [])
        return result