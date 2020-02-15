from collections import defaultdict


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
print(minSteps( "anagram", "mangaar"))

