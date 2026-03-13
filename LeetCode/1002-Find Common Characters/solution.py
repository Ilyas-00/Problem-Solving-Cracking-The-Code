# 1002. Find Common Characters
# O(n * m) time, where n is the number of words and m is the length of the longest word
# O(1) space, since the size of the array is fixed at 26
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        array_g = [0] * 26
        for letter in words[0]:
            array_g[ord(letter) - ord('a')] += 1

        for word in words[1:]:
            tempo = [0] * 26
            for letter in word:
                tempo[ord(letter) - ord('a')] += 1
            for i in range(26):
                array_g[i] = min(array_g[i], tempo[i])

        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * array_g[i])

        return result
    

# 1002. Find Common Characters

# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
 

# Constraints:
 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.