class Solution:
    def isValid(self, s: str) -> bool:
        opar = '''([{'''
        cpar = ''')]}'''
        stack = []
        for char in s:
            if char in opar:
                stack.append(char)

            elif char in cpar:
                if not stack:
                    return False

                elif cpar.index(char) != opar.index(stack.pop()):
                    return False

                

        return not stack