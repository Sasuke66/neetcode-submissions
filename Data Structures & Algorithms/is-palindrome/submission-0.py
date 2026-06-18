class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strins = s[::-1].lower()
        strins = "".join(char.lower() for char in s if char.isalnum())
        return strins == strins[::-1]