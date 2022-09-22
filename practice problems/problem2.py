class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        special = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        # base-case
        if len(s) <= 1: return lookup[s]
        # loop for rest
        output = 0
        i = 0
        while i < len(s):
            val = s[i:i+2]
            if val in special:
                i += 2
            else:
                output += lookup[s[i]]
                i += 1
        return output

s = Solution()
print(s.romanToInt("MCMXCIV"))