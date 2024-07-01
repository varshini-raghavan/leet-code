class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds=0
        for i in arr:
            if odds==3:
                return True
            if i%2!=0:
                odds+=1
            else:
                odds=0
        if odds==3:
            return True
        else:
            return False