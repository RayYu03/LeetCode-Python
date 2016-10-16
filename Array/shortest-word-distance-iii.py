# Time:  O(n)
# Space: O(1)
#
# This is a follow up of Shortest Word Distance.
# The only difference is now word1 could be the same as word2.
#
# Given a list of words and two words word1 and word2,
# return the shortest distance between these two words in the list.
#
# word1 and word2 may be the same and they represent two individual words in the list.
#
# For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = "coding", word2 = "practice", return 3.
# Given word1 = "makes", word2 = "coding", return 1.
#
# Note: You may assume that word1 does not equal to word2,
# and word1 and word2 are both in the list.
#

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestWordDistance(self, words, word1, word2):
        dist, i, index1, index2 = float("inf"), 0, None, None
        while i < len(words):
            if words[i] == word1:
                if index1 is not None:
                    dist = min(dist, abs(index1 - i))
                index1 = i
            elif words[i] == word2:
                index2 = i

            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))

            i += 1

        return dist

if __name__ == "__main__":
    result = Solution().shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")
    print result
