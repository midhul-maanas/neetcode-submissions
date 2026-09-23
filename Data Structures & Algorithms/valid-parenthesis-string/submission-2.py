class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        star = []
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if not stk and not star:
                    return False
                if stk:
                    stk.pop()
                else:
                    star.pop()
        while stk and star:
            if stk.pop() > star.pop():
                return False
        return not stk