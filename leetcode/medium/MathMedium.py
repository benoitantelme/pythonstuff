import itertools


def perm(tiles, temp, permutations: set):
    permutations.add(temp)
    for i in range(len(tiles)):
        perm(tiles[:i] + tiles[i + 1:], temp + tiles[i], permutations)


def numTilePossibilities(tiles: str) -> int:
    permutations = set()
    perm(tiles, "", permutations)
    return len(permutations) - 1


def numTilePossibilitiesItertools(tiles: str) -> int:
    sum = 0
    for n in range(1, len(tiles)+1):
        values = set(itertools.permutations(tiles, n))
        # print(values)
        sum += len(values)

    return sum


print(numTilePossibilities("AAB"))
# print(numTilePossibilities("AAABBC"))
