class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans,k=[],0
        def back(s,ans,k,temp=''):
            if k==4 and len(s)==0:# condition for valid IP address
                ans.append(temp[:-1])# to remove last dot
                return
            if k==4 or len(s)==0:# due to overflow IP address or not valid IP address
                return 
            for i in range(3):
                if k>4 or i+1>len(s): # overflow condition or due to loop for 3 times irrespective of input size
                    break
                if int(s[:i+1])>255: # not valid Ip address condition
                    continue
                if i!=0 and s[0]=="0": #to avoid "0.011.34.012" IP address
                    continue
                back(s[i+1:],ans,k+1,temp+s[:i+1]+'.')  # main logic with restore ip address
            return ans
        return back(s,ans,k,'')