class Solution:
    def guessNumber(self, n):
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            
            if res == 0:  # found it
                return mid
            elif res == -1:  # pick < mid
                right = mid - 1
            else:  # res == 1, pick > mid
                left = mid + 1