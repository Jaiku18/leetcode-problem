# Question:
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
#
# example:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

# Approach 1
# Explanation
# The question is to check whether the strings s follows the pattern,
# first we need to check whether  the length of pattern equals the  number of words the string contains if not true we
# can return the false since it wont match the pattern
# if the first condition passes we can move to the next one ie checking whether the len of unique character in pattern
# and words with that of the unique pattern created by combining these two strings,
#   Example:
# we can take Input: pattern = "abba", s = "dog cat cat dog"
#   len(set(pattern)) will contains len("ab") == 2
#  len(set(s)) will contains len(('dog', 'cat')) == 2
#  and len(set(zip(split_pater, pattern))) will contains len(set([('a', 'a'), ('b', 'b'), ('b', 'b'), ('a', 'a')])) == 2
# if they match then we can return the true else false

# Code
class Solution1:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_pater = s.split(" ")
        if len(pattern) != len(split_pater):
            return False
        return len(set(pattern)) == len(set(split_pater)) == len(set(zip(split_pater, pattern)))


# Approach 2
# Explanation
# Another approach for this problem is to use the inbuild function index which will return the index of the charcter in object
# we can use this function along with the map function to map each character index and obtain new index pattern
# if the new index_pattern for s and pattern matches then return True else return False
# Example
# we can take Input: pattern = "abba", s = "dog cat cat dog"
# map(s.index,s) will return [0,1,1,0] and map(pattern.index, pattern) will return [0,1,1,0]

class Solution2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s, new_pattern = s.split(), list(pattern)
        return map(s.index, s) == map(new_pattern.index, new_pattern)
