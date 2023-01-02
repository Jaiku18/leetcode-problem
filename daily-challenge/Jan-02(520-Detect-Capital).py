# We define the usage of capitals in a word to be right when one of the following cases holds:

# 1: All letters in this word are capitals, like "USA".
# 2: All letters in this word are not capitals, like "leetcode".
# 3: Only the first letter in this word is capital, like "Google".

# Given a string word, return true if the usage of capitals in it is right.

# Example Test Cases:

# 1:  Input: word = "USA"
#     Output: true

# 2:    Input: word = "FlaG"
#     Output: false

# Explanation:

# Approach 1
# The question says if the word is fully upper case or fully lower case we can return True for this we can use the inbuild
# methods isupper(), islower() to check whether the string is upper or lower resp once this is not true
# we can check omit the first character and check the rest of the characters are lower, in this way we can find if it is captialized or not


class Solution1:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        else:
            if word[1:].islower():
                return True
        return False

# Approach 2
# For this second approach we can avoid the below check by simply checking whether the word is capitalized version of
# the original word by using the inbuilt method capitalize


class Solution2:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or word == word.capitalize():
            return True
        return False
