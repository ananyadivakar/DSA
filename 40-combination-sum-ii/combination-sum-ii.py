class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Choose current number
                path.append(candidates[i])

                # Move to next index (cannot reuse same element)
                backtrack(i + 1, path, total + candidates[i])

                # Backtrack
                path.pop()

        backtrack(0, [], 0)
        return result