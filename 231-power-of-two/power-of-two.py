class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        def back(n):
            if n==2:
                return True
            elif n%2 !=0:
                return False
            else:
                return back(n//2)
        return back(n)
        
