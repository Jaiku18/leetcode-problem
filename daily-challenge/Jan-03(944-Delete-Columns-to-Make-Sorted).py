# You are given an array of n strings strs, all of the same length.
#
# The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

# abc
# bce
# cae
#
# You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
#
# Return the number of columns that you will delete.
#
# Example
#
# TestCase 1:
# Input: strs = ["cba","daf","ghi"]
# Output: 1
# Explanation: The grid looks as follows:
#   cba
#   daf
#   ghi
# Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
#
# TestCase 2:
# Input: strs = ["a","b"]
# Output: 0
# Explanation: The grid looks as follows:
#   a
#   b
# Column 0 is the only column and is sorted, so you will not delete any columns.


# Explaination:
# From the question we can understand we need to rearrange the given rows and columns, consider matrix where the rows and
# columns should be rearange and one more condition should be applied, the columns should be in the sorted ascendingly
#
# Approach One:
# in this approach we are just converting the rows into columns and comparing the columns whether it is sorted or not,
# for this we are using sorted() function

class Solution1:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0
        string_length = len(strs[0])
        sort_array = [''] * len(strs[0])
        for string in strs:
            for i in range(string_length):
                sort_array[i] += string[i]
        delete_count = 0
        for i in sort_array:
            if i != ''.join(sorted(i)):
                delete_count += 1
        return delete_count

# Approach Two:
#
# In this approach we are simply using zip function which will automatically zip the i character of every keyword,
# then we can compare whether the resulted string is in sorted order

class Solution2:
    def minDeletionSize(self, strs: List[str]) -> int:
        c = 0
        for i in zip(*strs):
            if list(i) != sorted(i):
                c += 1
        return c

