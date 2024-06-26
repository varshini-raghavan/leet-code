class Solution:
    def longestPalindrome(self, s: str) -> int:
        char=set()
        length=0
        for i in s:
            if i in char:
                char.remove(i)
                length+=2
            else:
                char.add(i)
        if char:
            length+=1
        
        return length