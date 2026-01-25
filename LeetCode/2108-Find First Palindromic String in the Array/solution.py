class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            # check if the word is the same words reversed 
            # " ".join(reversed(word)) is equivalent to word[::-1] (version slicing)
            if word == word[::-1]:
                return word
        return ""