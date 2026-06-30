class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # We just find how many characters we can find in the order over here
        right = 0
        curr_char = 0
        while right < len(s):
            if t[curr_char] == s[right]:
                curr_char += 1
                if curr_char == len(t):
                    break
            right += 1
        return len(t) - curr_char