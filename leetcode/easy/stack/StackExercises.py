

def removeOuterParentheses(S: str) -> str:
    count = 0
    res = ""
    for l in S:
        if l == '(':
            count += 1
            if count != 1:
                res += l
        else:
            count -= 1
            if count != 0:
                res += l
    return res


print(removeOuterParentheses("(()())(())"))


def removeDuplicates(S: str) -> str:
    stack = []
    previous = '@'
    for l in S:
        if previous == l:
            stack.pop()
            if len(stack) > 0:
                previous = stack[len(stack)-1]
            else:
                previous = '@'
        else:
            stack.append(l)
            previous = l
    return "".join(stack)


print(removeDuplicates("abbaca"))

