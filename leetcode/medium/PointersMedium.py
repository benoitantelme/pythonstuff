from typing import List


def findLast(S: str, c: chr) -> int:
    for i in range(len(S) - 1, -1, -1):
        if S[i] == c:
            return i


def partitionEnd(part: str) -> int:
    first = part[0]
    last = findLast(part, first)

    chars = set(part[:last + 1])
    chars.remove(first)

    while len(chars) > 0:
        c = chars.pop()
        lastc = findLast(part, c)
        if lastc > last:
            last = lastc
            chars = set(part[:last + 1])
            chars.remove(first)
            chars.remove(c)

    return last


def partitionLabels(S: str) -> List[int]:
    res = []
    end = -1
    size = len(S) - 1

    while len(S) > 0:
        end = partitionEnd(S) + 1
        res.append(end)
        S = S[end:]

    return res


print(partitionLabels("ababcbacadefegdehijhklij"))
