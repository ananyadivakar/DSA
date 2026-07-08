class Solution:
    def myAtoi(self, s):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Check if string is empty
        if i == n:
            return 0

        # Handle sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        # Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # Check overflow
            if num > (INT_MAX - digit) // 10:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num