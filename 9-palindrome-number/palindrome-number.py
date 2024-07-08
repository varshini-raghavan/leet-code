class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        rev=0
        temp=x
        while(x>0):
            rev=rev*10+x%10
            x=x//10
        if(temp==rev):
            return True
        else:
            return False
        