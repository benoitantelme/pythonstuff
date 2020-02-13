from typing import List
import heapq


def is_ascending(A):
    for i in range(0, len(A[0])):
        previous = 'a'
        for s in A:
            if s[i] < previous:
                return i
            previous = s[i]
    return -1


def minDeletionSize2(A: List[str]) -> int:
    init = len(A[0])
    it_is_not = is_ascending(A)
    while it_is_not != -1:
        for i in range(0, len(A)):
            A[i] = A[i][:it_is_not] + A[i][it_is_not + 1:]
            i += 1
        it_is_not = is_ascending(A)
    return init - len(A[0])


def minDeletionSize(A: List[str]) -> int:
    res = set()
    for j in range(len(A[0])):
        for i in range(len(A) - 1):
            if A[i][j] > A[i + 1][j]:
                res.add(j)
                break

    return len(res)


print(minDeletionSize(["cba", "daf", "ghi"]))
print(minDeletionSize(["a", "b"]))
print(minDeletionSize(["zyx", "wvu", "tsr"]))


def twoCitySchedCost(costs: List[List[int]]) -> int:
    a_or_b = []
    res = 0

    for cost in costs:
        if cost[0] < cost[1]:
            a_or_b.append(0)
            res += cost[0]
        else:
            a_or_b.append(1)
            res += cost[1]

    times = sum(a_or_b) - len(a_or_b) // 2
    if times == 0:
        return res

    updated_costs = []
    for i in range(0, len(costs)):
        if (times > 0 and a_or_b[i] == 1) or (times < 0 and a_or_b[i] == 0):
            updated_costs.append(costs[i])

    diff = []
    for cost in updated_costs:
        heapq.heappush(diff, abs(cost[0] - cost[1]))

    times = abs(times)
    for i in range(0, times):
        res += heapq.heappop(diff)

    return res


print(twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
print(twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]))
print(twoCitySchedCost(
    [[518, 518], [71, 971], [121, 862], [967, 607], [138, 754], [513, 337], [499, 873], [337, 387], [647, 917],
     [76, 417]]))
