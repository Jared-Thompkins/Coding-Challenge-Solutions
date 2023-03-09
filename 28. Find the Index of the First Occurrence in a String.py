class Solution:
    def strstr(self, haystack: str, needle: str):
        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
           if haystack[i: i + len(needle)] == needle:
               return i
        return -1