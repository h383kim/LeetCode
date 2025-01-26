################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
################################################################



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0

        maxLen = 0
        curLen = 0
        seen_char = set()

        while right < len(s):
            left_c, right_c = s[left], s[right]

            # if right pointer's character is not seen
            # keep increasing the right side of the window
            if right_c not in seen_char:
                seen_char.add(right_c)
                right += 1

            else:
                curLen = len(seen_char) # Measure length, as we'll start shrinking
                maxLen = max(curLen, maxLen) # Update if longer than longest
                right += 1
                while s[left] != right_c:
                    seen_char.remove(s[left])
                    left += 1
                left += 1
                continue
        
        maxLen = max(maxLen, len(seen_char))

        return maxLen 



