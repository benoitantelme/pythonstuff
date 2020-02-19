from collections import defaultdict, Counter
from typing import List
import sys


def minSteps(s: str, t: str) -> int:
    map = defaultdict(int)

    for l in s:
        map[l] += 1

    for l in t:
        if map[l] != 0:
            map[l] -= 1
            if map[l] == 0:
                map.pop(l)

    res = 0
    if len(map) != 0:
        for v in map.values():
            res += v

    return res


print(minSteps("bab", "aba"))
print(minSteps("leetcode", "practice"))
print(minSteps("anagram", "mangaar"))


def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
    dict = Counter(pattern)
    count_dict = Counter(dict.values())
    res = []

    for word in words:
        word_count = Counter(word)
        if count_dict != Counter(word_count.values()):
            continue

        m1, m2 = {}, {}
        same = True
        for w, p in zip(word, pattern):
            if w not in m1:
                m1[w] = p
            if p not in m2:
                m2[p] = w
            if (m1[w], m2[p]) != (p, w):
                same = False
                break
        if same:
            res.append(word)

    return res


print(findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))


def myAtoi(str: str) -> int:
    str = str.lstrip()

    if len(str) == 0:
        return 0

    # wrong start
    if str[0] != '-' and str[0] != '+' and ord('0') > ord(str[0]) or ord(str[0]) > ord('9'):
        return 0

    # clean left part of the string
    start = 0
    while str[start] != '-' and str[start] != '+' and ord('0') > ord(str[start]) or ord(str[start]) > ord('9'):
        start += 1
    str = str[start:]

    # set sign
    minus = False
    start = 0
    if str[0] == '-':
        minus = True
        start = 1
    elif str[0] == '+':
        start = 1

    # cut decimals
    if '.' in str:
        str = str.split('.')[0]

    # clean right part
    end = start
    while end < len(str) and ord('0') <= ord(str[end]) <= ord('9'):
        end += 1
    str = str[:end]

    # add
    res = 0
    for i in range(start, len(str)):
        if ord('0') > ord(str[i]) or ord(str[i]) > ord('9'):
            return 0
        res = res * 10 + (ord(str[i]) - ord('0'))

    # too long for 32 bits
    if abs(res) >= (2 ** 31):
        if minus:
            res = 2 ** 31
        else:
            res = 2 ** 31 - 1
    if minus:
        res *= -1

    return res


print(myAtoi("42"))
print(myAtoi("-42"))
print(myAtoi(" 4193 with words"))
print(myAtoi("with words 4193 with words"))
print(myAtoi("-91283472332"))
print(myAtoi("3.14159"))
print(myAtoi("+1"))
print(myAtoi("+-2"))
print(myAtoi("  -0012a42"))
print(myAtoi("2147483648"))
print(myAtoi("-5-"))
