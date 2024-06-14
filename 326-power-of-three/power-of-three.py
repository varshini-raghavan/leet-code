class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        def back(n):
            if n==3:
                return True
            if n<3:
                return False
            else:
                return back(n/3)
        return back(n)
        
