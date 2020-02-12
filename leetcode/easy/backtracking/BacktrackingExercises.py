from typing import List


def letterCasePermutationRec(S, res, chars, start):
    if start >= len(S):
        res.append(chars)
        return

    l = S[start]
    if l.isalpha():
        letterCasePermutationRec(S, res, chars + l.upper(), start+1)
        letterCasePermutationRec(S, res, chars + l.lower(), start+1)
    else:
        chars += l
        letterCasePermutationRec(S, res, chars, start+1)


def letterCasePermutation2(S: str) -> List[str]:
    res = []
    letterCasePermutationRec(S, res, '', 0)

    return res


def letterCasePermutation(S: str) -> List[str]:
    res = ['']
    i = 0
    for l in S:
        if l.isalpha():
            new = []
            for index, val in enumerate(res):
                new.append(val + l.lower())
                res[index] = val + l.upper()
            res.extend(new)
        else:
            for index, val in enumerate(res):
                res[index] = val + l

    return res


print(letterCasePermutation("a1b2"))
