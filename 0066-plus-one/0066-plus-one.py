class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        buf = 1
        for i in range(len(digits)-1,-1,-1):
            if buf + digits[i] == 10:
                digits[i] = 0
                buf = 1
            else:
                digits[i] += 1
                buf = 0
                break

        if buf:
            digits.insert(0,1)
        return digits
        
