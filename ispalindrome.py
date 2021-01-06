class Solution(object):
    def isPalindrome(self, x):
    
        if pow(-2, 31) >= x or x >= pow(2,31)-1 or x < 0:
            return False
        else:
            placeholder = x
            reversed_num = 0
            while placeholder > 0:
                n = placeholder % 10
                reversed_num = reversed_num * 10 + n
                placeholder = placeholder // 10
            if reversed_num == x:
                return True
            else:
                return False

num = int(input("Input: "))

print(f"Output: {Solution.isPalindrome(bool ,num)}")