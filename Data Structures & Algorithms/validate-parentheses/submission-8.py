class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            
            if i in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                character = stack.pop()

                match i:
                    case ')':
                        if character != '(':
                            return False
                    case '}':
                        if character != '{':
                            return False
                    case ']':
                        if character != '[':
                            return False
        if len(stack) == 0:
            return True
        else:
            return False