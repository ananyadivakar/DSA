class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            line_words = []
            line_length = 0

            # Put as many words as possible in the line
            while i < len(words):
                word = words[i]

                if line_length + len(word) + len(line_words) > maxWidth:
                    break

                line_words.append(word)
                line_length += len(word)
                i += 1

            # Last line or only one word
            if i == len(words) or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)
                continue

            # Calculate spaces
            total_spaces = maxWidth - line_length
            gaps = len(line_words) - 1

            space = total_spaces // gaps
            extra = total_spaces % gaps

            line = ""

            for j in range(gaps):
                line += line_words[j]
                line += " " * (space + (1 if j < extra else 0))

            line += line_words[-1]
            result.append(line)

        return result