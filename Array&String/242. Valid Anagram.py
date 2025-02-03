################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/valid-anagram/
################################################################


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = {}, {}
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
        

        for k,v in dict_s.items():
            if k not in dict_t:
                return False
            if dict_s[k] != dict_t[k]:
                return False
            del dict_t[k]
        
        if dict_t:
            return False

        return True