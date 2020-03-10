from typing import List


class Solution:
    result = []

    def recAllPathsSourceTarget(self, graph: List[List[int]], node: int, path: List[int]):
        tmp = path.copy()
        tmp.append(node)

        neighbours = graph[node]
        for i in neighbours:
            if i == len(graph) - 1:
                tmp2 = tmp.copy()
                tmp2.append(i)
                self.result.append(tmp2)
                continue
            else:
                self.recAllPathsSourceTarget(graph, i, tmp)

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        self.recAllPathsSourceTarget(graph, 0, [])

        return self.result

    def find(self, parents: List[int], i: int) -> int:
        if parents[i] == -1:
            return i
        else:
            return self.find(parents, parents[i])

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [-1] * (len(set([item for edge in edges for item in edge])) + 1)
        for edge in edges:
            x = self.find(parents, edge[0])
            y = self.find(parents, edge[1])

            # loop
            if x == y:
                return edge
            parents[x] = y
        return None


s = Solution()
# print(s.allPathsSourceTarget([[1, 2], [3], [3], []]))
print(s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
print(s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
print(s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
