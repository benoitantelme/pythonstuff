from collections import defaultdict, Counter
from typing import List


def numJewelsInStones(J: str, S: str) -> int:
    result = 0
    for l in (l for l in S if l in J):
        result += 1

    return result


print(numJewelsInStones("aA", "aAAbbbb"))


def repeatedNTimes(A: List[int]) -> int:
    bound = len(A)//2
    times = defaultdict(int)
    for a in A:
        times[a] += 1
        if times[a] >= bound:
            return a


print(repeatedNTimes([1, 2, 3, 3]))
print(repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))


def uniqueOccurrences(arr: List[int]) -> bool:
    count = Counter(arr)
    if len(count.values()) == len(set(count.values())):
        return True
    else:
        return False


print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print(uniqueOccurrences([1, 2]))
print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))


def subdomainVisits(cpdomains: List[str]) -> List[str]:
    visits = defaultdict(int)
    for cpdomain in cpdomains:
        splitted = cpdomain.split()
        domains = splitted[1]
        while len(domains) > 1:
            visits[domains] += int(splitted[0])
            domains = domains.partition('.')[2]

    result = []
    for k, v in visits.items():
        result.append(str(v) + ' ' + k)
    return result


print(subdomainVisits(["9001 discuss.leetcode.com"]))
print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1).intersection(set(nums2)))


print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))

