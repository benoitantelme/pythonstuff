from collections import defaultdict, Counter
from typing import List


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
