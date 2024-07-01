class Solution:
    def trailingZeroes(self, n: int) -> int:
        fac=1
        while n>0:
            fac*=n
            n-=1
        nzero=0
        while fac>0:
            last=fac%10
            fac=fac//10
            if last==0:
                nzero+=1
            else:
                break
        return nzero