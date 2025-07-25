class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int) -> int:
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in cols or (row - col) in diag or (row + col) in anti:
                    continue
                cols.add(col)
                diag.add(row - col)
                anti.add(row + col)
                count += backtrack(row + 1)
                cols.remove(col)
                diag.remove(row - col)
                anti.remove(row + col)
            return count

        cols = set()
        diag = set()
        anti = set()
        return backtrack(0)

                 

