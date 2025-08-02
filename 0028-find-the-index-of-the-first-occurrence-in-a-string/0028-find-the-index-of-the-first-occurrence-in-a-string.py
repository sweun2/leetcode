class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            start = 0
            while start < len(needle) and haystack[i + start] == needle[start]:
                start += 1
            
            if start == len(needle):
                return i
        
        return -1