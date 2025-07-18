class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
        def dfs(temp:List[int], cur):
            result.append(temp[:])
            for i in range(cur, len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    temp.append(nums[i])
                    dfs(temp, i + 1)

                    visited.remove(nums[i])
                    temp.remove(nums[i])
        
        dfs([],0)
        return result