class Solution:
    def mySqrt(self, x: int) -> int:
        cnt = 0
        re = 0
        while re <= x:
            cnt +=1
            re = cnt * cnt

        return cnt -1