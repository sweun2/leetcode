class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
                cnt -=1
        nums.sort()    
        return cnt
            

    
