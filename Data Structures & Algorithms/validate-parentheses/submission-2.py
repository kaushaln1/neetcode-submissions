class Solution:
    def isValid(self, s: str) -> bool:
        s=list(s)
        stack= []
        for char in s :
            if char == ")" and len(stack) != 0  :
                c1 = stack.pop()
                if c1 != "(":
                    return False
                continue
            if char == "}" and len(stack) != 0:
                c2 = stack.pop()
                if c2 !="{":
                    return False
                continue
            
            if char == "]" and len(stack) != 0: 
                c3 = stack.pop()
                if c3 !="[":
                    return False
                continue
            
            stack.append(char)
        
        if len(stack) == 0:
            return True 
        else:
            return False



        