from typing import List


def divisorGame2(N: int) -> bool:
    """
    1 loose
    2 1 win
    3 2 1 loose
    4 3 2 1 win
    5 4 3 2 1 loose
    6 3 2 1 win
    """
    first_win = False
    while N > 1:
        for i in range(N - 1, 0, -1):
            if N % 2 == 0:
                N = N - 1
            if N % i == 0:
                N = N - i
                first_win = not first_win
                break
    return first_win


def divisorGame(N: int) -> bool:
    return N % 2 == 0


print(divisorGame(2))
print(divisorGame(3))
print(divisorGame(4))
print(divisorGame(5))
print(divisorGame(6))


def climbStairs(n: int) -> int:
    """
    fibonacci really
    """
    a = 1
    b = 2
    if n == 1:
        return a
    if n == 2:
        return b
    while n > 2:
        c = a + b
        a = b
        b = c
        n -= 1
    return b


print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(5))
print(climbStairs(6))


def minCostClimbingStairs(cost: List[int]) -> int:
    a = cost[0]
    b = cost[1]
    for i in range(2, len(cost)):
        a, b = b, min(a, b) + cost[i]
    return min(a, b)


print(minCostClimbingStairs([10, 15, 20]))
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(minCostClimbingStairs([0, 2, 2, 1]))
print(minCostClimbingStairs([0, 1, 2, 0]))

