class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        index = start
        temp = set()
        max_v = 0
        while start < len(s):
            if index == len(s):
                max_v = max(max_v,len(temp))
                return max_v

            if s[index] not in temp:
                temp.add(s[index])
                index += 1
            else:
                max_v = max(max_v, len(temp))
                
                start += 1
                index = start
                temp.clear()
        return max_v