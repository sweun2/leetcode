class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        temp = set()
        maxv = 0
        for i in range(len(s)):
            while s[i] in temp:
                temp.remove(s[left])
                left +=1
            temp.add(s[i])
            maxv = max(maxv,i-left+1)
    
        return maxv