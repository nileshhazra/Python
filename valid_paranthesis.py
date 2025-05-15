class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last == "(" and char != ")":
                    return False
                if last == "{" and char != "}":
                    return False
                if last == "[" and char != "]":
                    return False

        if len(stack) != 0:
            return False
        else:
            return True
