class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        index = 0
        cnt = 0
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                cnt +=1
                index +=1
                nums[index] = nums[i]
        return cnt + 1
                
