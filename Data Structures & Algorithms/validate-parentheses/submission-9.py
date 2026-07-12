class Solution:
    def isValid(self, s: str) -> bool:
        stk=['X']
        d = {')':'(', ']':'[', '}':'{'}
        if len(s) <= 1:
            return False
        for i in s:
            if i in ['{','(','[']:
               stk.append(i)
               print(f'Stack status: {stk}')
            if i in d:
                if stk[-1] == d[i]:
                    stk.remove(d[i])
                    print(f"Stack status:{stk}")
                else:
                    return False  
        if len(stk) == 1 and stk[0] == 'X':
            return True
        return False