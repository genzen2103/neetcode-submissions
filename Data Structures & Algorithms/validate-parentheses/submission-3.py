class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        matching = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for c in s:
            if c in '[({':
                temp.append(c)
            else:
                if not temp or temp[-1] != matching[c]:
                    return False
                temp.pop()    
        return len(temp)==0
