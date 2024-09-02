self =0
x=121


class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = int(str(x)[::-1])
        if x == rev:
            return True
        else:
            return False
    print(isPalindrome(self,x))