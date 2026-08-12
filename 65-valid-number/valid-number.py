class Solution:
    def isNumber(self, s):
        digit_seen = False
        dot_seen = False
        e_seen = False

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                digit_seen = True

            elif ch == '.':
                if dot_seen or e_seen:
                    return False
                dot_seen = True

            elif ch == 'e' or ch == 'E':
                if e_seen or not digit_seen:
                    return False
                e_seen = True
                digit_seen = False

            elif ch == '+' or ch == '-':
                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False

            else:
                return False

        return digit_seen