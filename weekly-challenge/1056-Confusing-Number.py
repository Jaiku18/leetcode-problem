# A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.
#
# We can rotate digits of a number by 180 degrees to form new digits.
#
# When 0, 1, 6, 8, and 9 are rotated 180 degrees, they become 0, 1, 9, 8, and 6 respectively.
# When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid.
# Note that after rotating a number, we can ignore leading zeros.
#
# For example, after rotating 8000, we have 0008 which is considered as just 8.
# Given an integer n, return true if it is a confusing number, or false otherwise.

# Example test cases:
#
# Input: n = 6
# Output: true
# Explanation: We get 9 after rotating 6, 9 is a valid number, and 9 != 6.
#
# Input: n = 89
# Output: true
# Explanation: We get 68 after rotating 89, 68 is a valid number and 68 != 89.
#
# Input: n = 11
# Output: false
# Explanation: We get 11 after rotating 11, 11 is a valid number but the value remains the same,
# thus 11 is not a confusing number

# Explanation
# the first check is to find whether the numbers in the n contains invalid confusion number ie 2,3,4,5,7, if yes return False
# if the number doesn't have invalid confusion number then we need to ratate the number by 180 is reverse with a simple twist
# as you know while rotating 0, 1, 8 the result will be the same, the trick part arrives while rotating 6 and 9,
# since they both return 9 and 6 resp after rotation to find this we need to maintain an mapping dict with the
# actual value and rotating values and then reverse the number based on rotating

class Solution:
    def confusingNumber(self, n: int) -> bool:
        confusing_number_mapping = {0: 0, 1: 1, 8: 8, 6: 9, 9: 6}
        copy_number = n
        reverse_number = 0
        while n > 0:
            remainder = n % 10
            if remainder not in confusing_number_mapping:
                return False
            reverse_number = (reverse_number * 10) + confusing_number_mapping[remainder]
            n //= 10
        if copy_number == reverse_number:
            return False
        return True
