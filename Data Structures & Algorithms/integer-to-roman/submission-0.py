class Solution:
    def intToRoman(self, num: int) -> str:
        #  list of (value, symbol) pairs, sorted biggest to smallest. 
        symList = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
            ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
            ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
            ["M", 1000]
        ]
        res = ""
        for sym, val in reversed(symList):
            count = num // val
            if count:
                res += sym * count
                num %= val
        return res
        # define the possibles:
        # thousands = ["", "M", "MM", "MMM"]
        # hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        # tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        # ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        # return (
        #     thousands[num // 1000] +
        #     hundreds[(num % 1000) // 100] +
        #     tens[(num % 100) // 10] +
        #     ones[num % 10]
        # )