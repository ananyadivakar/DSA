class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(index, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target or index == len(candidates):
                return

            # Include current candidate
            current.append(candidates[index])
            backtrack(index, current, total + candidates[index])

            # Backtrack
            current.pop()

            # Exclude current candidate
            backtrack(index + 1, current, total)

        backtrack(0, [], 0)
        return result