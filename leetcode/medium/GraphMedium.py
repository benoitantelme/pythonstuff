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


s = Solution()
# print(s.allPathsSourceTarget([[1, 2], [3], [3], []]))
print(s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
