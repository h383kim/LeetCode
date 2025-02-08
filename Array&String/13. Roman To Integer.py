################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/roman-to-integer/
################################################################



class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        num = 0
        i = 0
        while i < len(s):
            c = s[i]
            if i == len(s) - 1:
                return num + roman_dict[c]
            
            c_next = s[i + 1]
            
            if roman_dict[c] < roman_dict[c_next]:
                diff = roman_dict[c_next] - roman_dict[c]
                num += diff
                i += 2
            else:
                num += roman_dict[c]
                i += 1

        return num