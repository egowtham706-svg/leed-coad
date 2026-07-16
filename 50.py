class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        
        # handle negative n
        if n < 0:
            x = 1 / x
            n = -n
        
        ans = 1
        while n > 0:
            # if n is odd, multiply ans by x
            if n % 2 == 1:
                ans = ans * x
            # square x and halve n
            x = x * x
            n = n // 2
        
        return ans