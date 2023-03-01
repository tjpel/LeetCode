class Solution():
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            prefix = strs[0]

            for s in strs[1:]:
                while prefix != s[:len(prefix)]:
                    prefix = prefix[:-1]
                    
            return prefix
        
s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "floght"]))

        