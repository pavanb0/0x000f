class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        if len(tokens)<=1:
            return int(tokens[-1])
        operators=[
            '+',
            '-',
            '*',
            '/'
        ]
        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                if i=='+':
                    p=stack.pop()
                    j=stack.pop()
                    stack.append(int(p)+int(j))
                    
                if i=='/':
                    p=stack.pop()
                    j=stack.pop()
                    stack.append(int(int(j)/int(p)))
                    
                if i=='*':
                    p=stack.pop()
                    j=stack.pop()
                    stack.append(int(p)*int(j))
                    
                if i=='-':
                    p=stack.pop()
                    j=stack.pop()
                    stack.append(int(j)-int(p))
                    

        return stack[-1]
