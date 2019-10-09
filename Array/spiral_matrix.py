class Solution:
    def generateMatrix(self, n: int):
        it = iter(range(1, n ** 2 + 1))
        m = [[None] * n for x in range(n)]
        return self.generate_matrix_rec(m, it, 0, n - 1, 0, n - 1)

    def generate_matrix_rec(self, m, it, row_start, row_stop, col_start, col_stop) -> List[List[int]]:
        # This is our base case:
        if row_start > row_stop:

            # when n is even:
            return m
        if row_start == row_stop:
            # when n is odd:
            m[row_start][col_start] = next(it)
            return m

        # Fill in the top:
        for col in range(col_start, col_stop):
            m[row_start][col] = next(it)
        # Fill in the right side:
        for row in range(row_start, row_stop):
            m[row][col_stop] = next(it)
        # Fill in the bottom:
        for col in range(col_stop, col_start, -1):
            m[row_stop][col] = next(it)
        # Fill in the left side:
        for row in range(row_stop, row_start, -1):
            m[row][col_start] = next(it)

        # Chop off the top/right/bottom/left sides, and repeat on the inner matrix:
        #

        return self.generate_matrix_rec(m, it, row_start + 1, row_stop - 1, col_start + 1, col_stop - 1)