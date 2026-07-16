class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)

            if i == ')':
                if len(stack) == 0:
                    return False
                character = stack.pop()
                if character != '(':
                    return False
            if i == '}':
                if len(stack) == 0:
                    return False
                character = stack.pop()
                if character != '{':
                    return False
            if i == ']':
                if len(stack) == 0:
                    return False
                character = stack.pop()
                if character != '[':
                    return False
        if len(stack) == 0:
            return True
        else:
            return False