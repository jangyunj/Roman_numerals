#1 Approach---------------------------
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        number = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[(i + 1)]]:
                number -= roman[s[i]]
            else:
                number+= roman[s[i]]
        return number + roman[s[-1]]
    

#roman[s] -- s is the variable for str that we enter
#s[i] -- parsing of the input string -- loops
#Then checks if that value is lower than the value of the next key. If yes, subtract, if no, add.
#Last element is always added to not including in the loop

#2 Approach-----------------------------
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII") \
             .replace("IX", "VIIII") \
             .replace("XL", "XXXX") \
             .replace("XC", "LXXXX") \
             .replace("CD", "CCCC") \
             .replace("CM", "DCCCC") \
             
        return sum(map(translations.get, s))
    
#3 Approach---------------------------------
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number