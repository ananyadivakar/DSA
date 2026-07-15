class Solution(object):
    def processStr(self, s, k):
        n = len(s)

        # lengths[i] = length after processing first i characters
        lengths = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = lengths[i]

            if 'a' <= ch <= 'z':
                lengths[i + 1] = cur + 1

            elif ch == '*':
                lengths[i + 1] = max(0, cur - 1)

            elif ch == '#':
                lengths[i + 1] = cur * 2

            else:  # '%'
                lengths[i + 1] = cur

        if k >= lengths[n]:
            return '.'

        # Work backwards
        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev_len = lengths[i]

            if 'a' <= ch <= 'z':
                if k == prev_len:
                    return ch

            elif ch == '#':
                if prev_len > 0:
                    k %= prev_len

            elif ch == '%':
                k = prev_len - 1 - k

            # '*' requires no change to k when moving backwards

        return '.'