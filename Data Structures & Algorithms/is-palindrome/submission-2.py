class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower= s.isalnum()
        s_lower=''.join([char for char in s if char.isalnum()]).lower()
        return s_lower[::-1]==s_lower

        