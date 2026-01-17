class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        row1_set = set(row1)
        row2_set = set(row2)
        row3_set = set(row3)

        # w = words.lower()
        # letters = set(w)
        res = []
        for w in words : 
            s = set(w.lower())
            if s <= row1_set : 
                res.append(w)
            elif s <= row2_set : 
                res.append(w)
            elif s <= row3_set : 
                res.append(w)
        return res


# 500. Keyboard Row

# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

 

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]

# Output: ["Alaska","Dad"]

# Explanation:

# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

# Example 2:

# Input: words = ["omk"]

# Output: []

# Example 3:

# Input: words = ["adsdf","sfd"]

# Output: ["adsdf","sfd"]

 

# Constraints:

# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase). 
 
