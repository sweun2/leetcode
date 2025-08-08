class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        visited = set()

        for i in nums:
            if i not in visited:
                visited.add(i)
                if nums.count(i) > n/2:
                    return i
            else:
                continue
