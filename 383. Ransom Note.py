class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        ran = sorted(list(ransomNote))
        mag = sorted(list(magazine))

        for c in mag:
            if ran and c == ran[0]:
                ran.pop(0)
        if ran:
            return False
        else:
            return True