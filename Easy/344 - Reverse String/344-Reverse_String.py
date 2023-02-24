class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        print(s)

s = Solution()
s.reverseString(["T", "h", "o", "m", "a", "s"])