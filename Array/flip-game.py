# Time:  O(c * n + n) = O(n * (c+1))
# Space: O(n)
#
#
# You are playing the following Flip Game with your friend:
# Given a string that contains only these two characters: + and -,
# you and your friend take turns to flip twoconsecutive "++" into "--".
# The game ends when a person can no longer make a move and
# therefore the other person will be the winner.
#
# Write a function to compute all possible states of
# the string after one valid move.
#
# For example, given s = "++++", after one move,
# it may become one of the following states:
#
#    [
#      "--++",
#      "+--+",
#      "++--"
#    ]
#
# If there is no valid move, return an empty list [].



# This solution compares only O(1) times for the two consecutive "+"
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        i, n = 0, len(s) - 1
        while i < n:
            if s[i] == '+':
                while i < n and s[i + 1] == '+':
                    res.append(s[:i] + '--' + s[i+2:])
                    i += 1
            i += 1

        return res

# Time:  O(c * m * n + n) = O(c * n + n), where m = 2 in this question
# Space: O(n)
# This solution compares O(m) = O(2) times for two consecutive "+", where m is length of the pattern
class Solution2(object):
  def generatePossibleNextMoves(self, s):
      """
      :type s: str
      :rtype: List[str]
      """
      return [s[:i] + "--" + s[i+2:] for i in xrange(len(s) - 1) if s[i:i+2] == '++']

if __name__ == '__main__':
    result = Solution2().generatePossibleNextMoves('++++++')
    print result
