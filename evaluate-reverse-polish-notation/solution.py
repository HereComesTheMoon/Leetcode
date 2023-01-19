class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
        for token in tokens:
            match token:
                case '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b + a)
                case '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                case '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)
                case '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(trunc(b / a))
                case _:
                    stack.append(int(token))
        
        return stack.pop()
