'''
#1 Task 1 - Easy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
'''

'''
#2 Task 9 - Easy
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
# Second variation
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original_x = x
        reversed_x = 0
        while x > 0:
            digit = x % 10  
            reversed_x = reversed_x * 10 + digit  
            x //= 10  
        if original_x == reversed_x:
            return True
        else:
            return False
'''

'''
#3 Task 13 - Easy
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for char in reversed(s):
            current_value = roman_numerals[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        return total
'''

s = input()
output = ""
current_pofl = 0
max_rofl = 0

for i in range(len(s)):
    if i == 0:
        output += s[i]
    elif s[i] in output:
        if max_rofl < len(output):
            max_rofl = len(output)
        output = ""
        output += s[i]
    else:
        output += s[i]

if max_rofl < len(output):
    max_rofl = len(output)

print(output)
print(max_rofl)