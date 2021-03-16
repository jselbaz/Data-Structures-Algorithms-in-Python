class Solution:

    def longestPalindrome(self, str):
        result = ""        
        for i in range(len(str)):
            word1 = self.checkPalindrome(str, i, i) #check for odd number of letters
            word2 = self.checkPalindrome(str, i, i+1) #check for even number of letters
            
            if len(word1) >= len(word2):
                longest = word1
            else:
                longest = word2
                
            if len(longest) >= len(result):
                result = longest
            else:
                result = result
            
        return result          
        
            
    def checkPalindrome(self, str, left, right):
        
        while left >= 0 and right < len(str) and str[left] == str[right]:
            left -= 1
            right += 1
        
        return str[left+1:right]