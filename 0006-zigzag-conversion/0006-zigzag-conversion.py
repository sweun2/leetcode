class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result_str = ["" for i in range(numRows)]

        index = 0
        direction = 1
        for i in range(len(s)):
            result_str[index] += (s[i])
            index = index + direction

            if index == numRows-1 or index == 0:
                direction *= -1
        return "".join(result_str)


            
        