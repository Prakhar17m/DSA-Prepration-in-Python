class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        for oper in operations:
            if oper=='+':
                stk.append(stk[-1]+stk[-2])
            elif oper =='D':
                stk.append(stk[-1]*2)
            elif oper== 'C':
                stk.pop()
            else:
                stk.append(int(oper))
        return sum(stk)