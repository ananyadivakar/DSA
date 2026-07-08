from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7

        pos = []
        vals = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                vals.append(int(ch))

        k = len(vals)

        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        prefNum = [0] * (k + 1)
        prefSum = [0] * (k + 1)

        for i in range(1, k + 1):
            prefNum[i] = (prefNum[i - 1] * 10 + vals[i - 1]) % MOD
            prefSum[i] = prefSum[i - 1] + vals[i - 1]

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1
            number = (prefNum[right + 1] - prefNum[left] * pow10[length]) % MOD
            digit_sum = prefSum[right + 1] - prefSum[left]

            ans.append((number * digit_sum) % MOD)

        return ans