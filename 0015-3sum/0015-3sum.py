class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.add((nums[i] , nums[left] , nums[right]))
                    left +=1
                    right -=1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left +=1
                else:
                    right -=1

        return list(result)