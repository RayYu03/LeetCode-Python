# Time:  O(n)
# Space: O(1)

# Given a non-empty string s and an abbreviation abbr,
# return whether the string matches with the given abbreviation.
#
# A string such as "word" contains only the following valid abbreviations:
#
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2",
# "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
#
# Notice that only the above abbreviations are valid abbreviations of
# the string "word". Any other string is not a valid abbreviation of "word".
#
# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.
#
# Example 1:
#
# Given s = "internationalization", abbr = "i12iz4n":
#
# Return true.
#
#
# Example 2:
#
# Given s = "apple", abbr = "a2e":
#
# Return false.

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, digit = 0, 0
        for c in abbr:
            if c.isdigit():
                if digit == 0 and c == '0':
                    return False
                digit *= 10
                digit += int(c)
            else:
                if digit:
                    i += digit
                    digit = 0
                if i >= len(word) or word[i] != c:
                    return False
                i += 1

        if digit:
            i += digit
        return i == len(word)

if __name__ == "__main__":
    print Solution().validWordAbbreviation("Hail Hydra",'5Hydra')
