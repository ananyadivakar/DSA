class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_index = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in last_index and last_index[ch] >= left:
                left = last_index[ch] + 1

            last_index[ch] = right
            ans = max(ans, right - left + 1)

        return ans