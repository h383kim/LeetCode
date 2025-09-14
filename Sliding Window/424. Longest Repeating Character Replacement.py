################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/longest-repeating-character-replacement/
################################################################




class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countDict = defaultdict(int)
        maxLen = 0
        l, r = 0, 0

        for _ in range(len(s)):
            c = s[r]
            countDict[c] += 1

            while ((r - l + 1) - max(countDict.values())) > k:
                countDict[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen
