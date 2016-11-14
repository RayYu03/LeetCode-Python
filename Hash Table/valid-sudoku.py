# Time:  O(9^2)
# Space: O(9)

# Determine if a Sudoku is valid,
# according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled,
# where empty cells are filled with the character '.'.
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable.
# Only the filled cells need to be validated.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # validate if has same number in one line or one row
        for i in xrange(9):
            if not self.isValidList([board[i][j] for j in xrange(9)]) or \
               not self.isValidList([board[j][i] for j in xrange(9)]):
               return False

        # validate if has same number in every cube of 9*9
        for i in xrange(3):
            for j in xrange(3):
                if not self.isValidList([board[m][n] for n in xrange(3 * j, 3 * j + 3) \
                                                     for m in xrange(3 * i, 3 * i + 3)]):
                    return False
        return True

    def isValidList(self, xs):
        xs = filter(lambda x:x != '.', xs)
        return len(set(xs)) == len(xs)
