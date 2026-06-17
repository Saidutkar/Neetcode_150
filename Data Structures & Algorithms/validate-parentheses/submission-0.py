class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {}
        par_dict[']'] = '['
        par_dict['}'] = '{'
        par_dict[')'] = '('

        par_stack = []

        for ch in s:
            if ch in par_dict.keys():
                if par_stack and par_stack[-1] == par_dict[ch]:
                    par_stack.pop()
                else:
                    return False
            else:
                par_stack.append(ch)

        return True if len(par_stack) == 0 else  False
        