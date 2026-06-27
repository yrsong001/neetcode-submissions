class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # work on string from the back, and use a map
        map = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }
        integer = 0
        
        # i = 1
        # while i < len(s)+1:
        #     if i < len(s) and map[s[-(i+1)]] < map[s[-i]]:
        #         integer = integer + map[s[-i]] - map[s[-(i+1)]]
        #         i += 2
        #     else:
        #         integer = integer + map[s[-i]]
        #         i += 1
        # return integer

        # For each Roman symbol, compare it with the symbol immediately to its right. If it is smaller, subtract it. Otherwise, add it.
        for i in range(len(s)):
            if i < len(s)-1 and map[s[(i+1)]] > map[s[i]]:
               integer -= map[s[i]]
            else: integer += map[s[i]]
        return integer


        