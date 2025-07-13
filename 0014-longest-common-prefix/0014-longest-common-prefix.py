class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shorts = min(strs)
        if not strs:
            return ""
        length = 0
        result = ""
        while length < len(shorts):
            flag = False
            cur = shorts[length]
            for s in strs:
                if len(s) < length or s[length] != cur:
                    return result
            result += cur
            length += 1                
    
        return result
        