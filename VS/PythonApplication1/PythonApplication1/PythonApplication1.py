'''
#1 Task 1 - Easy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
'''

#2 Task 9 - Easy
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
# Second 
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