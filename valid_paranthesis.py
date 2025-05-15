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

    def isValid2(self, s):
        stack = []
        pairs = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if pairs[last] != char:
                    return False

        if len(stack) > 0:
            return False
        else:
            return True


def main():
    sol = Solution()
    res1 = sol.isValid("[]({})")
    res2 = sol.isValid2("[{(}]")
    print(res1, res2)


if __name__ == "__main__":
    main()
