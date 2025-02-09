################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/integer-to-roman/
################################################################



class Solution:
    def intToRoman(self, num: int) -> str:
        str_num = str(num)
        # Extracting digits
        if num > 0:
            one_digit = int(str_num[-1])
        else: one_digit = 0
        if num >= 10:
            ten_digit = int(str_num[-2])
        else: ten_digit = 0
        if num >= 100:
            hund_digit = int(str_num[-3])
        else: hund_digit = 0
        if num >= 1000:
            thou_digit = int(str_num[-4])
        else: thou_digit = 0

        roman = ''
        # Thousands
        if thou_digit > 0:
            roman = roman + 'M' * thou_digit

        # Hundreds
        if hund_digit > 0:
            if hund_digit == 4:
                roman = roman + 'CD'
            elif hund_digit == 9:
                roman = roman + 'CM'
            else:
                if hund_digit > 4:
                    roman = roman + 'D'
                roman = roman + 'C' * (hund_digit % 5)

        # Tens
        if ten_digit > 0:
            if ten_digit == 4:
                roman = roman + 'XL'
            elif ten_digit == 9:
                roman = roman + 'XC'
            else:
                if ten_digit > 4:
                    roman = roman + 'L'
                roman = roman + 'X' * (ten_digit % 5)
        
        # Ones
        if one_digit > 0:
            if one_digit == 4:
                roman = roman + 'IV'
            elif one_digit == 9:
                roman = roman + 'IX'
            else:
                if one_digit > 4:
                    roman = roman + 'V'
                roman = roman + 'I' * (one_digit % 5)
            
        return roman