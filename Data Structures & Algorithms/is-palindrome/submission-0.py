class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).strip().lower()

        l = 0
        r = len(s) - 1

        while l != r and l < len(s) and r > 0:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True