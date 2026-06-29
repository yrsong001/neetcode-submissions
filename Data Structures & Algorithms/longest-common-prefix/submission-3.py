class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the shortest string
        # Loop through its characters by position
        # Check if all other strings have the same character at that position
        # Stop and return when they don't

        # find the shortest
        # shortest = strs[0]
        # for i in strs:
        #     if len(i) < shortest:
        #         shortest = i
        shortest = min(strs, key=len)  # Python finds shortest string for you

        for i in range(len(shortest)):
            for j in strs: 
                if shortest[i] != j[i]:
                    return shortest[:i]
        return shortest
        # for i in strs: # if campare all together we cannot shrink
        #     if shortest != i[:len(shortest)]:
        #         return False

