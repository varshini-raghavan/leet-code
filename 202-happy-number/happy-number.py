class Solution:
    def isHappy(self, n: int) -> bool:
        def sumdigi(n):
            n=str(n)
            sum=0
            for i in n:
                sum+=int(i)**2
            return sum
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n=sumdigi(n)
        return n==1

