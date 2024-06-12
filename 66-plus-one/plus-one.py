class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in digits:
            num=num*10+i
        num+=1
        ans=[]
        while num>0:
            ans.append(num%10)
            num=num//10
        return ans[::-1]