class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close=[')','}',']']
        for i in s:
            if not len(stack) and i in close:
                return False
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            elif i==')' and stack[-1]=='(':
                stack.pop()
            elif i=='}' and stack[-1]=='{':
                stack.pop()
            elif i==']' and stack[-1]=='[':
                stack.pop()
            else:
                return False
        if len(stack):
            return False
        return True
            



        