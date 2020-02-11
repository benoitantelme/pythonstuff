from collections import defaultdict
from typing import List


def findJudge(N: int, trust: List[List[int]]) -> int:
    trust_dict = defaultdict(list)
    for l in trust:
        trust_dict[l[1]].append(l[0])
    for i in range(1, N + 1):
        somewhere = False
        for values in trust_dict.values():
            if i in values:
                somewhere = True
                break
        if not somewhere and len(trust_dict[i]) == N - 1:
            return i

    return -1


print(findJudge(3, [[1, 3], [2, 3]]))
print(findJudge(3, [[1, 3], [2, 3], [3, 1]]))
