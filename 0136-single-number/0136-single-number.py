class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = set()
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                temp.remove(i)
        
        return list(temp)[0]
