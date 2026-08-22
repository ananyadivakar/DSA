class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = {}

        required = len(need)
        formed = 0

        left = 0
        min_len = float("inf")
        min_left = 0

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            # Character requirement is now satisfied
            if char in need and window[char] == need[char]:
                formed += 1

            # Try shrinking the window
            while formed == required:
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                left_char = s[left]
                window[left_char] -= 1

                # Removing this character makes the window invalid
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[min_left:min_left + min_len]