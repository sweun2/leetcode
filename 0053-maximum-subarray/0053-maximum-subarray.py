class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global maxv
        maxv = 0
        
        def dac(start, end):
            if start == end:
                return nums[start]
            
            mid = (start+end)//2

            left_max = dac(start,mid)
            right_max = dac(mid+1,end)

            left_sum = -1000000000
            cur = 0
            for i in range(mid,start-1,-1):
                cur += nums[i]
                left_sum = max(left_sum,cur)
            
            right_sum = -1000000000
            cur = 0
            for i in range(mid+1,end+1):
                cur += nums[i]
                right_sum = max(right_sum,cur)

            cross = left_sum + right_sum

            return max(cross,left_max,right_max)
        
        return dac(0,len(nums)-1)


