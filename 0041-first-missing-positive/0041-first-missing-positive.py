class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        cnt = 1
        for i in nums:
            if i > 0:
                if cnt == i:
                    cnt +=1
                else:
                    break
        return cnt
        
                    

